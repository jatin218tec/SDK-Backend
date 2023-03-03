from rest_framework.response import Response
from pymongo.errors import OperationFailure

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import json
import uuid


def addSubcollection(request, client):
    """
    Add a sub-collection to a document in a collection.
    @param request - the request object
    @param client - the client object
    @returns a response object
    """
    data = request.data

    collection_name = data.get('collection_name', None)
    document_id = data.get('document_id', None)
    sub_collection_name = data.get('sub_collection_name', None)
    subdocuments_data = request.data.get('document_data')

    # checking 404
    if not collection_name:
        return Response({"error": "No collection name specified."}, status=400)
    if not sub_collection_name:
        return Response({"error": "No sub collection specified."}, status=400)
    if not subdocuments_data:
        return Response({"error": "No data to add."}, status=400)

    subdocuments_data = json.loads(subdocuments_data)

    # Use the collection name in the URL to select the correct model
    db_store = client.get_database("store")
    db_sub_store = client.get_database("sub_store")

    collection = db_store.get_collection(collection_name)
    sub_collection = db_sub_store.get_collection(sub_collection_name)

    try:
        if collection.count_documents({}) == 0:
            return Response({"error": "Collection not found."}, status=404)
        else:
            subdocuments_data["document_id"] = document_id
            subdocuments_data["collection_id"] = collection_name

            if "_id" not in subdocuments_data:
                subdocuments_data["_id"] = str(uuid.uuid4())

            sub_document = sub_collection.insert_one(subdocuments_data)
            s_id = sub_document.inserted_id

            # Update document instance with the data from the request
            document = collection.update_one(
                {"_id": document_id},
                {"$set": {f"sub_collection_{sub_collection_name}_id": s_id}}
            )
            return Response({"success": True, "message": f"sub-collection created :)"})
    except OperationFailure as e:
        return Response({"success": False, "message": e}, status=500)


def addDocument(request, client):
    """
    Add a document to the database.
    @param request - the request object           
    @param client - the client object           
    @returns a response object           
    """
    data = request.data

    collection_name = data.get('collection_name', None)
    document_data = data.get('document_data', None)
    project_id = data.get('project_id', None)

    # checking 404
    if not collection_name:
        return Response({"error": "No collection name specified."}, status=400)
    if not document_data:
        return Response({"error": "No data to add."}, status=400)

    document_data = json.loads(document_data)

    # Use the collection name in the URL to select the correct model
    db = client.get_database("store")

    collection = db.get_collection(collection_name)

    try:
        # Create a new document instance with the data from the request
        if "_id" not in document_data:
            document_data["_id"] = str(uuid.uuid4())

        channel_layer = get_channel_layer()

        collection_data = collection.find({}).limit(10)

        async_to_sync(channel_layer.group_send)(
            f'{project_id}_{collection_name}',
            {
                "type": "websocket.collection",
                "collection": collection_data
            })

        document = collection.insert_one(document_data)

        collection_data = collection.find({}).limit(10)

        async_to_sync(channel_layer.group_send)(
            f'{project_id}_{collection_name}',
            {
                "type": "websocket.collection",
                "collection": collection_data
            })

        return Response({"success": True, "message": f"Inserted document with id: {document.inserted_id}"})

        # return Response({"success": True, "message": f"Inserted document with id: {document.inserted_id}"})

    except OperationFailure as e:
        return Response({"success": False, "message": e}, status=500)

def updateDocument(request, client):
    data = request.data

    collection_name = data.get('collection_name', None)
    document_data = data.get('document_data', None)
    project_id = data.get('project_id', None)

    # checking 404
    if not collection_name:
        return Response({"error": "No collection name specified."}, status=400)
    if not document_data:
        return Response({"error": "No data to update."}, status=400)

    document_data = json.loads(document_data)
    if not document_data:
        return Response({"error": "No document specified."}, status=400)
    
    document_id = document_data["_id"]

    doc_data_dict = {k: v for k, v in document_data.items() if k != '_id'}

    try:
        # Use the collection name in the URL to select the correct model
        db = client.get_database("store")

        collection = db.get_collection(collection_name)
        collection.update_one({
            {"_id": document_id},
            {"$set": doc_data_dict}    
        })

        channel_layer = get_channel_layer()
        document_data = collection.find({"_id": document_id})

        async_to_sync(channel_layer.group_send)(
            f'{project_id}_{collection_name}_{document_data["_id"]}',
            {
                "type": "documents.update",
                "document": document_data
            })

        return Response({"success": True, "message": f"Inserted document with id: {document_id}"})

    except OperationFailure as e:
        return Response({"success": False, "message": e}, status=500)
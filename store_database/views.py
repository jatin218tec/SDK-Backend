from rest_framework.views import APIView
from mongoengine import Document, EmbeddedDocument, fields
from mongoengine import StringField, IntField, FloatField, DateTimeField, ListField, DictField
from rest_framework.response import Response

from authentication.utils import APIKeyAuthentication, ProjectPermission
import json

from mongoengine import connect, disconnect

from . import helper

client = connect(host="mongodb+srv://jatin21ai:wZMjBcTb2No6TpRO@cluster1.bxuv5nq.mongodb.net/?retryWrites=true&w=majority", name="store")


# class CollectionCreateAPI(APIView):

#     authentication_classes = [APIKeyAuthentication]
#     permission_classes = [ProjectPermission]


#     def post(self, request, *args, **kwargs):
#         collection_name = request.data.get('collection_name')
#         db = client.get_database("store")

#         collection_names = db.list_collection_names()
#         print(collection_names)
#         if collection_name.lower() in collection_names:
#             disconnect()
#             return Response({"error": f"Collection with name {collection_name} already exist."}, status=409)
#         else:
#             fields = request.data.get('fields')
#             fields = json.loads(fields)

#             document_data = request.data.get('document_data')
#             document_data = json.loads(document_data)

#             if not collection_name:
#                 return Response({"error": "No collection name specified."}, status=400)
#             if not fields:
#                 return Response({"error": "No fields specified."}, status=400)

#             # Create a new document model for the collection
#             fields_dict = {field['name']: self.get_field_type(field['type']) for field in fields}

#             Collection = type(collection_name.capitalize(),
#                               (Document,), fields_dict)
#             Collection.objects.create(**document_data)

#             disconnect()
            
#             return Response({"success": True})

#     def get_field_type(self, type_str):
#         if type_str == 'string':
#             return StringField()
#         elif type_str == 'datetime':
#             return DateTimeField()
#         elif type_str == 'list':
#             return ListField()
#         elif type_str == 'int':
#             return IntField()
#         elif type_str == 'dict':
#             return DictField()
#         elif type_str == 'float':
#             return FloatField()
        

class AddSubCollectionAPIView(APIView):

    authentication_classes = [APIKeyAuthentication]
    permission_classes = [ProjectPermission]

    def post(self, request, *args, **kwargs):
        response = helper.addSubcollection(request, client)
        return response


class AddDocumentAPIView(APIView):

    authentication_classes = [APIKeyAuthentication]
    permission_classes = [ProjectPermission]

    def post(self, request, *args, **kwargs):
        response = helper.addDocument(request, client)
        return response
    
    def put(self, request, *args, **kwargs):
        response = helper.updateDocument(request, client)
        return response
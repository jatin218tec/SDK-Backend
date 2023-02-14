from django.urls import path
from .views import CollectionCreateAPI, AddDocumentAPIView

urlpatterns = [
    path('create-collection/', CollectionCreateAPI.as_view(), name='create-collection'),
    path('add-document/', AddDocumentAPIView.as_view(), name='add-document')
]
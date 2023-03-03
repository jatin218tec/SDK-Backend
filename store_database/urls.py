from django.urls import path
from .views import AddDocumentAPIView, AddSubCollectionAPIView

urlpatterns = [
    path('add-document/', AddDocumentAPIView.as_view(), name='add-document'),
    path('update-document/', AddDocumentAPIView.as_view(), name='add-document'),
    path('create-sub-collection/', AddSubCollectionAPIView.as_view(), name='create-collection'),
]
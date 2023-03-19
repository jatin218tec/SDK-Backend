from django.urls import path
from .views import DocumentAPIView, AddSubCollectionAPIView

urlpatterns = [
    path('add-document/', DocumentAPIView.as_view(), name='add-document'),
    path('update-document/', DocumentAPIView.as_view(), name='add-document'),
    path('delete-document/<str:document>', DocumentAPIView.as_view(), name='delete-document'),
    path('create-sub-collection/', AddSubCollectionAPIView.as_view(), name='create-collection'),
]
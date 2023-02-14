from django.urls import path
from .views import SignInView, ProjectRetrieveUpdateDestroyView, ProjectCreateView

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('projects/<str:pk>', ProjectRetrieveUpdateDestroyView.as_view(), name='project-details'),
    path('projects/', ProjectCreateView.as_view(), name='project'),
]
from django.urls import path
from .views import SignUpView, ProjectRetrieveUpdateDestroyView, ProjectCreateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('projects/<str:pk>', ProjectRetrieveUpdateDestroyView.as_view(), name='project-details'),
    path('projects/', ProjectCreateView.as_view(), name='project'),
]
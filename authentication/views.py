from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer, ProjectSerializer
from .utils import APIAuthentication
from .models import Projects, UserProfile

# auth views
class SignInView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.save()
# project views
class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [APIAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    
class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [APIAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

class ProjectCreateView(generics.ListCreateAPIView):
    
    permission_classes = [AllowAny]

    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
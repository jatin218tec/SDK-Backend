from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

class SignInView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        user.key = uuid.uuid4().hex
        user.save()

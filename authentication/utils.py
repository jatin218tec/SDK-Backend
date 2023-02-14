from rest_framework import authentication
from rest_framework.permissions import BasePermission
from rest_framework import exceptions
from .models import Projects, UserProfile

class APIAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        api_key = request.data.get('api_key')
        if api_key:
            try:
                project = Projects.objects.get(api_key=api_key)
            except Projects.DoesNotExist:
                raise exceptions.AuthenticationFailed('Invalid API key')
            return (project, None)
        raise exceptions.AuthenticationFailed('API key is required')
    
class ProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, UserProfile):
            return request.user.is_authenticated
        return True
from rest_framework import authentication
from .models import CustomUser

class KeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        key = request.META.get('HTTP_API_KEY')
        if not key:
            return None
        try:
            user = CustomUser.objects.get(key=key)
        except user.DoesNotExist:
            return None
        return (user, None)

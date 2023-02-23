from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from djangorestapitest2 import settings
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
      token = request.META.get('HTTP_AUTHORIZATION')
      error_msg = "internal error"

      if not token:
        error_msg = "There is not token on auth, use Bearer Token Auth"
        raise AuthenticationFailed(error_msg)

      try:
        token = Token.objects.get(key=token.split(" ")[1])
        if token.created+settings.AUTH_TOKEN_VALIDITY > timezone.now():
          return (token.user, None)
        else:
          print("2?")
          error_msg = "Token has expired"
      except Token.DoesNotExist:
        error_msg = "Token doesn't exists"
      
      raise AuthenticationFailed(error_msg)


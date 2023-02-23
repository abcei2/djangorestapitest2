from ui.custom_auth import CustomAuthentication
from ui.models import CustomUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
import json


@api_view(['GET'])
@authentication_classes([CustomAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)


@api_view(['POST'])
def login(request, format=None):
  login_data = json.loads(request.body)
  try:
    logged_in_user = CustomUser.objects.get(email=login_data["email"], password=login_data["password"])
  
    token = Token.objects.get_or_create(user=logged_in_user)
    print("?", token[1])
    return Response(token[0].key)
  except:
    return Response("Wrong credentials1")

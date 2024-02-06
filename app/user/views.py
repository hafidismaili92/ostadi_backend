from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from user.serializers import CreateTokenSerializer, UserSerializer
from rest_framework.settings import api_settings

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """Create User in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    serializer_class =  CreateTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
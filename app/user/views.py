from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from user.serializers import CreateTokenSerializer, UserSerializer
from rest_framework.settings import api_settings

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """Create User in the system"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create and return a token """
    serializer_class =  CreateTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class MyProfilView(generics.RetrieveAPIView):
    """Get Profil informations of current authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
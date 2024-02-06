from rest_framework import generics

from user.serializers import UserSerializer


# Create your views here.

class CreateUserView(generics.CreateAPIView):
    """Create User in the system"""
    serializer_class = UserSerializer
    
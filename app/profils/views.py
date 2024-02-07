
from rest_framework import generics
from profils.serializers import LevelSerializer, SubjectSerializer

from profils.models import Level, Subject

# Create your views here.

class SubjectsList(generics.ListAPIView):
    """Retrieve list of all Subjects"""
    queryset = Subject.objects.order_by('id').all()
    serializer_class = SubjectSerializer

class LevelsList(generics.ListAPIView):
    """Retrieve list of all Levels"""
    queryset = Level.objects.order_by('id').all()
    serializer_class = LevelSerializer
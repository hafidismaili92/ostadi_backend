
from rest_framework import viewsets, authentication
from core.auth.custom_permissions import IsStudent,IsProfessor
from jobs.serializers import JobPostSerializer

from jobs.models import JobPost

class AllJobPostsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsProfessor]
    
    def get_queryset(self):
        return self.queryset.order_by('-id')

class MyJobPostsViewSet(viewsets.ModelViewSet):
    queryset = JobPost.objects.all()
    serializer_class = JobPostSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsStudent]

    def get_queryset(self):
        return self.queryset.filter(student=self.request.user.student_account).order_by('-id')
    
    def perform_create(self,serializer):
        """create a new jobPost"""
        #add the student that own this jobpost (the current connected user)
        serializer.save(student=self.request.user.student_account)

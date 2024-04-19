from rest_framework import serializers

from user.models import User
from profils.models import Student, Subject
from jobs.models import Duration, JobPost, JobProposal

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']
        
class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Student
        fields = ['id', 'user']

class DurationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Duration
        fields = ['id','duration']
class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['title']

class JobPostSerializer(serializers.ModelSerializer):
    
    '''student = StudentSerializer()
    duration = DurationSerializer()
    subjects = SubjectSerializer(many=True)'''
    class Meta:
        model = JobPost
        fields='__all__'
        read_only_fields = ['id','student']
        extra_kwargs={
            'subjects':{
                'required':False
            },
            
        }

class JobProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobProposal
        fields = '__all__'
        read_only_fields = ['id','proposed_by']
    
    
    
        
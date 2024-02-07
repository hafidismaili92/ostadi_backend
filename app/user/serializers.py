from rest_framework import serializers
from django.contrib.auth import (get_user_model, authenticate)
from django.utils.translation import gettext as _
from profils.models import Professor, Student
from profils.serializers import ProfessorSerializer, StudentSerializer

from user.models import User

class UserSerializer(serializers.ModelSerializer):
    
    student_account = StudentSerializer(required=False)
    professor_account = ProfessorSerializer(required=False)
    #sd=StudentSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('name','email','password','student_account','professor_account','is_default_student','is_student','is_professor')
        extra_kwargs= {"password":{'write_only':True,'min_length':8},"is_default_student":{'read_only':True},"is_student":{'read_only':True},"is_professor":{'read_only':True}}
        
    
    def create(self, validated_data):
        
        """Create and return a user with encrypted password"""
        
        if 'student_account' in validated_data:
            level = validated_data.pop('student_account')['level']
            #level = Level.objects.get(id=level_id)
            student = Student.objects.create(level=level)
            return get_user_model().objects.create_user(student_account=student,**validated_data,is_default_student=True)
        elif 'professor_account' in validated_data:
            subjects = validated_data.pop('professor_account')['subjects']
            professor = Professor.objects.create()
            professor.subjects.set(subjects)
            return get_user_model().objects.create_user(professor_account=professor,**validated_data)
        else:
            return None

class CreateTokenSerializer(serializers.Serializer):
    """login user and create token"""
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_style':'password'},trim_whitespace=False)

    def validate(self,attrs):
        email = attrs['email']
        password = attrs['password']

        user = authenticate(
            request= self.context.get('request'),
            email = email,
            password = password
        )

        if not user:
            msg = _('unable to login with provided credentials')
            raise serializers.ValidationError(msg,code='Authorization')
        
        attrs['user'] = user
        return attrs

    
        
    
    
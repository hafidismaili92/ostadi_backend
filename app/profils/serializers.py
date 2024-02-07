from rest_framework import serializers

from profils.models import Level, Professor, Student, Subject


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('id','title',)
        
        extra_kwargs= {"title":{'read_only':True},"id":{'read_only':True}}

class StudentSerializer(serializers.ModelSerializer):
    level_id = serializers.PrimaryKeyRelatedField(queryset=Level.objects.all(), source='level', write_only=True)
    level = LevelSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ('level','level_id',)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id','title','icon')
        
        extra_kwargs= {"title":{'read_only':True},"id":{'read_only':True},"icon":{'read_only':True}}

class ProfessorSerializer(serializers.ModelSerializer):
    subjects_ids = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), source='subjects', write_only=True,many=True)
    subjects = SubjectSerializer(read_only=True,many=True)
    class Meta:
        model = Professor
        fields = ('subjects','subjects_ids',)
    
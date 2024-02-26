from rest_framework import serializers

from jobs.models import JobPost

class JobPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobPost
        fields = '__all__'
        read_only_fields = ['id','student']
    
    
        
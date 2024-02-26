from django.db import models

from profils.models import Student, Subject

class Duration(models.Model):
    duration = models.CharField(max_length=255)

    def __str__(self):
        return self.duration
    
class JobPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.ForeignKey(Duration, on_delete=models.SET_NULL,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject,blank=True)

    def __str__(self):
        return self.title

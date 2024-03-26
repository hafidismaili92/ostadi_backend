from django.db import models

# Create your models here.

class Level(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title.title()

class Subject(models.Model):
    title=models.CharField(max_length=200)
    icon =models.ImageField(upload_to="images/subjects")

    def __str__(self):
        return self.title.title()
    

class Student(models.Model):
    level = models.ForeignKey(Level,on_delete = models.SET_NULL,null=True)

    def __str__(self):
        return self.user.email

class Professor(models.Model):
    subjects = models.ManyToManyField(Subject)
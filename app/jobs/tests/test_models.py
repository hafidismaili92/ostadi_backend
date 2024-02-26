from django.test import TestCase
from jobs.models import Duration, JobPost
from profils.models import Student,Level


     
class TestJobModel(TestCase):
    """a class to test JobTest model crud"""

    @classmethod
    def setUpTestData(cls):
        payloadslevel1 = {
            "title":"test level 1"
        }
        first_level = Level.objects.create(**payloadslevel1)
        cls.student = Student.objects.create(level=first_level)
        cls.duration = Duration.objects.create(duration="less than 1 month")
    def test_create_jobPost_success(self):
        """test create a jobpost by a student success"""
        #arrange
        payloads = {
            "title":"test jobPost",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        }
        #act
        job = JobPost.objects.create(student=self.student,duration=self.duration,**payloads)

        #assert
        self.assertEqual(job.student.id,self.student.id)
        self.assertEqual(job.title,payloads['title'])

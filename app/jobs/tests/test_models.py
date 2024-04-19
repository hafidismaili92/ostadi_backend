from django.test import TestCase
from jobs.models import Duration, JobPost, JobProposal
from profils.models import Professor, Student,Level, Subject


     
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

class TestProposalModel(TestCase):
    '''a class to test the proposal model (creating, updating,.......)'''

    @classmethod
    def setUpTestData(cls):
        #create a student and a job from this student

        payloadslevel1 = {
            "title":"test level 1"
        }
        first_level = Level.objects.create(**payloadslevel1)
        student = Student.objects.create(level=first_level)
        duration = Duration.objects.create(duration="less than 1 month")
        cls.duration = duration
        payloadsJob = {
            "title":"test jobPost",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        }
        
        cls.job = JobPost.objects.create(student=student,duration=duration,**payloadsJob)
        #create a professor
        payloadssubj1 = {
            "title":"test subject 1","icon":"test icon 1"
        }
        payloadssubj2 = {
            "title":"test subject 2","icon":"test icon 2"
        }
        first_subject = Subject.objects.create(**payloadssubj1)
        second_subject = Subject.objects.create(**payloadssubj2)
        cls.professor = Professor.objects.create()
        cls.professor.subjects.set([first_subject.id,second_subject.id])

    def test_create_proposal_success(self):
        '''test that creation a proposal success'''
        payloads = {
            "description":"test description",
            "amount":522,
        }

        proposal = JobProposal.objects.create(proposed_by=self.professor,post=self.job,**payloads)

        #assert
        self.assertEqual(proposal.proposed_by.id,self.professor.id)
        self.assertEqual(proposal.description,payloads["description"])
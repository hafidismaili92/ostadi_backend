from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from jobs.models import Duration, JobPost, JobProposal
from profils.models import Level, Professor, Student, Subject
from user.models import User

PROPOSAL_API_URL = reverse('jobs:my-proposals-list')
class TestProposalsApiAuthenticatedUser(TestCase):
    """test of proposal api (add , update.......)"""
    @classmethod
    def setUpTestData(cls):
        payloadslevel1 = {
            "title":"test level 1"
        }
        first_level = Level.objects.create(**payloadslevel1)
        cls.student = Student.objects.create(level=first_level)
        duration = Duration.objects.create(duration="less than 1 month")
        cls.duration = duration
        payloadsJob = {
            "title":"test jobPost",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        }
        
        cls.job = JobPost.objects.create(student=cls.student,duration=duration,**payloadsJob)
        #create a professor
        cls.professor = Professor.objects.create()
        cls.professorUser = User.objects.create_user(email="testst@example.com",password="testpassword",name="testprof",professor_account=cls.professor)
        
        
    def setUp(self) :
        self.client = APIClient()
        self.client.force_authenticate(user=self.professorUser)

    def test_create_proposal_api(self):
        newProposalPayLoads = {
            "description":"test description",
            "amount":522,
            "post":self.job.id,
            
        }
        response = self.client.post(PROPOSAL_API_URL,newProposalPayLoads)
        #assert
        
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_create_proposal_by_not_prof_failed(self):
        newProposalPayLoads = {
            "description":"test description",
            "amount":522,
            "post":self.job.id,
            
        }
        studentClient = APIClient()
        studentUser = User.objects.create_user(email="teststst@example.com",password="testpassword",name="teststudent",student_account=self.student)
        studentClient.force_authenticate(user=studentUser)

        response = studentClient.post(PROPOSAL_API_URL,newProposalPayLoads)
        #assert
        
        self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)



    def test_get_my_proposal_list_api_success(self):

        otherprof = Professor.objects.create()


        myfirstproposalpayloads = {
            "description":"first test description",
            "amount":522,
            
        }
        mysecondproposalpayloads = {
            "description":"second test description",
            "amount":24,
            
        }
        notMyProposal = {
            "description":"not my proposal description",
            "amount":240,
            
        }
        firstproposal = JobProposal.objects.create(post=self.job,proposed_by=self.professor,**myfirstproposalpayloads)
        secondproposal = JobProposal.objects.create(post=self.job,proposed_by=self.professor,**mysecondproposalpayloads)
        notMyproposal = JobProposal.objects.create(post=self.job,proposed_by=otherprof,**notMyProposal)

        response = self.client.get(PROPOSAL_API_URL)
        #assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        self.assertNotContains(response,"not my proposal description")
    
    


class TestProposalsPublic(TestCase):
    @classmethod
    def setUpTestData(cls):
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

    def test_create_proposal_faild(self):
        newProposalPayLoads = {
            "description":"test description",
            "amount":522,
            "post":self.job.id,
            
        }
        response = self.client.post(PROPOSAL_API_URL,newProposalPayLoads)
        #assert
        
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    
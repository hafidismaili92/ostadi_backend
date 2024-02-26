from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from jobs.models import Duration, JobPost


from user.models import User

from profils.models import Level, Student

MY_JOBPOSTS_URL = reverse('jobs:my-jobPosts-list')
ADD_JOBPOST_URL = reverse('jobs:my-jobPosts-list')

class TestJobPostsApiAuthenticatedUser(TestCase):
    """test jobposts api (get job lists, create, jobpost, update......) for authenticated user"""
    @classmethod
    def setUpTestData(cls):
        #create a student user and force authenticate
        cls.level = Level.objects.create(title='Test Level')
        studentAccount = Student.objects.create(level=cls.level)
        cls.studentUser = User.objects.create_user(email="testst@example.com",password="testpassword",name="testuser",student_account=studentAccount)
        
        
        cls.duration = Duration.objects.create(duration="less than 1 month")
    
    def setUp(self) :
        self.client = APIClient()
        self.client.force_authenticate(user=self.studentUser)
    def test_MyJobPosts_list_success(self):
        #arrange
        jobpostsPayloads = [{
            "title":"test jobPost 1",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        },{
            "title":"test jobPost 2",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        }]
        for arg in jobpostsPayloads:
            JobPost.objects.create(student=self.studentUser.student_account,duration=self.duration,**arg)
        
        #act
        response = self.client.get(MY_JOBPOSTS_URL)
        
        #assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        self.assertEqual(response.data[1]['title'],jobpostsPayloads[0]['title'])

    def test_jobPostList_contains_only_authUser_jobs(self):
        anotherStudentAccount = Student.objects.create(level=self.level)
        anotherstudentUser = User.objects.create_user(email="teststudent2@example.com",password="testpassword",name="testuser",student_account=anotherStudentAccount)
        
        authenticatedUserjobpostsPayloads = [{
            "title":"test jobPost 1",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        },{
            "title":"test jobPost 2",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        }]
        for arg in authenticatedUserjobpostsPayloads:
            JobPost.objects.create(student=self.studentUser.student_account,duration=self.duration,**arg)

        # create a jobpost for another user
        anotherUserJobPayload = {
            "title":"test jobPost 3",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        }
        
        JobPost.objects.create(student=anotherstudentUser.student_account,duration=self.duration,**anotherUserJobPayload )

        #act
        response = self.client.get(MY_JOBPOSTS_URL)
        
        #assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),2)
        self.assertNotContains(response,"test jobPost 3")
    
    def test_create_jobPost_success(self):
        #arrange
        JobPayload = {
            "title":"test jobPost 3",
            "description":"""Tempor amet aliqua amet pariatur sit voluptate minim consectetur in. Occaecat in enim commodo nulla commodo. Dolore tempor culpa sunt velit commodo
            voluptate laboris. Commodo elit quis amet sunt ex labore magna eu qui mollit sint proident. Ex laboris dolor magna minim pariatur fugiat quis excepteur mollit. Tempor 
            officia nostrud et officia esse deserunt anim tempor dolore.""",
            
            "amount":500
        }
        #act
        response = self.client.post(ADD_JOBPOST_URL,JobPayload)
        print(response.data)
        #assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)


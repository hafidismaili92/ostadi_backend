
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from user.models import User
from profils.models import Level, Professor, Student, Subject
from rest_framework.test import APIClient
from rest_framework import status



CREATE_USER_URL = reverse('user:create')
GET_TOKEN_URL = reverse('user:token')
GET_MYPROFIl_URL = reverse('user:me')

class PublicTestUser(TestCase):
    """a class to test user managements (create, login, .....)"""
    
    def setUp(self):
        self.client = APIClient()


    def test_create_student_success(self):
        """test creating new user type sudent"""
        
        #arrange
        level = Level.objects.create(title='Test Level')
        payloadStudent = {
            "name":"test name",
            "email":"test@example.com",
            "password":"passwordtest",
            "student_account":{
                'level_id':level.id
            }
        }
       
        #act
        res = self.client.post(CREATE_USER_URL,payloadStudent,format="json")

        #assert
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        tuser = get_user_model().objects.get(email=payloadStudent["email"])
        self.assertTrue(tuser.check_password(payloadStudent["password"]))
        tstudent = tuser.student_account
        self.assertEqual(tstudent.level.id,payloadStudent["student_account"]["level_id"])
    
    def test_create_Professor_success(self):
        """test creating new user type professor"""
        
        #arrange
        first_subject = Subject.objects.create(title="test subject 1",icon="test icon 1")
        second_subject = Subject.objects.create(title="test subject 2",icon="test icon 2")

        payloadProf = {
            "name":"test name",
            "email":"test@example.com",
            "password":"passwordtest",
            "professor_account":{
                'subjects_ids':[first_subject.id,second_subject.id]
            }
        }
       
        #act
        res = self.client.post(CREATE_USER_URL,payloadProf,format="json")

        #assert
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        tuser = get_user_model().objects.get(email=payloadProf["email"])
        self.assertTrue(tuser.check_password(payloadProf["password"]))
        tprof = tuser.professor_account
        self.assertEqual(list(tprof.subjects.all()),[first_subject,second_subject])

    def test_user_with_email_exist_error(self):
        """error returned if user with email exist"""
        #arrange
        payload = {
            'email':'test@exemple.com',
            'password':'testpass123',
            'name': 'Test 2 Name'
        }
        """create a user with above email"""
        get_user_model().objects.create_user(**payload)
        
        #act
        """recreate a user with above email"""
        res = self.client.post(CREATE_USER_URL,payload)
        #assert
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertTrue(user_exists)
    
    def test_user_short_password_error(self):
        """error returned if user with email exist"""
        payload = {
            'email':'testpassword@exemple.com',
            'password':'pw',
            'name': 'Test 2 Name'
        }
        res = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(user_exists)
    
    def test_create_token_success(self):
        #arrange
        payloads ={'email':'test@example.com','password':'testpassword'}
        user = get_user_model().objects.create_user(**payloads)

        #act

        res = self.client.post(GET_TOKEN_URL,payloads)

        #assert
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        
        self.assertIn('token',res.data)

    def test_UnauthenticatedUser_get_profil_failed(self):
        res = self.client.get(GET_MYPROFIl_URL)
        #assert
        self.assertEqual(res.status_code,status.HTTP_401_UNAUTHORIZED)
    
class AuthenticatedUserTest(TestCase):
    """test operations that needs authendicated user to be performed"""

    def setUp(self):
        self.client = APIClient()
        level = Level.objects.create(title='Test Level')
        studentAccount = Student.objects.create(level=level)
        self.studentUser = User.objects.create_user(email="testst@example.com",password="testpassword",name="testuser",student_account=studentAccount)
        profAccount = Professor.objects.create()
        first_subject = Subject.objects.create(title="test subject 1",icon="test icon 1")
        second_subject = Subject.objects.create(title="test subject 2",icon="test icon 2")
        profAccount.subjects.set([first_subject.id,second_subject.id])
        self.profUser= User.objects.create_user(email="testpr@example.com",password="testpassword",name="testprof",professor_account=profAccount)
        
        #self.client.force_login(self.profUser)
    def test_get_student_myprofil_success(self):

        #act
        self.client.force_authenticate(user = self.studentUser)
        res = self.client.get(GET_MYPROFIl_URL)
        #assert
        
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data['email'],self.studentUser.email)
        self.assertEqual(res.data['name'],self.studentUser.name)
    
    def test_get_prof_myprofil_success(self):

        #act
        self.client.force_authenticate(user = self.profUser)
        res = self.client.get(GET_MYPROFIl_URL)
        #assert
        print(res.data)
        self.assertEqual(res.status_code,status.HTTP_200_OK)
        self.assertEqual(res.data['email'],self.profUser.email)
        self.assertEqual(res.data['name'],self.profUser.name)
    
    def test_post_me_not_allowed(self):
        """test POST is not allowed on me endpoint"""
        self.client.force_authenticate(user = self.studentUser)
        res = self.client.post(GET_MYPROFIl_URL,{})

        self.assertEqual(res.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)


    
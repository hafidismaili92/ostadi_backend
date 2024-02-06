
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from profils.models import Level, Subject
from rest_framework.test import APIClient
from rest_framework import status
from user.serializers import UserSerializer

CREATE_USER_URL = reverse('user:create')


class PublicTestUser(TestCase):
    """a class to test user managements (create, login, .....)"""
    
    def setUp(self):
        self.client = APIClient()


    def test_create_student(self):
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
        serializer = UserSerializer(data=payloadStudent)
        #act
        res = self.client.post(CREATE_USER_URL,payloadStudent)

        #assert
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        tuser = get_user_model().objects.get(email=payloadStudent["email"])
        self.assertTrue(tuser.check_password(payloadStudent["password"]))
        tstudent = tuser.student_account
        self.assertEqual(tstudent.level.id,payloadStudent["student_account"]["level_id"])

    # def test_create_professor(self):
    #     """test creating new user type Professor"""
    #     first_subject = Subject.objects.create(title="test subject 1",icon="test icon 1")
    #     second_subject = Subject.objects.create(title="test subject 2",icon="test icon 2")

    #     payloadProf = {
    #         "name":"test name",
    #         "email":"test@example.com",
    #         "password":"passwordtest",
    #         "professor_account":{
    #             'subjects_ids':[first_subject.id,second_subject.id]
    #         }
    #     }
    #     #arrange
    #     serializer = UserSerializer(data=payloadProf)
    #     if serializer.is_valid():
            
    #         user = serializer.save()
    #         serializerv = UserSerializer(instance=user)
    #         serialized_data = serializerv.data
    #         print(serialized_data)
    #         #assert
    #         #self.assertEqual(user.student_account.level.id,payloadStudent["student_account"]['level_id'])
    #         #self.assertTrue(user.check_password(payloadStudent["password"]))
        
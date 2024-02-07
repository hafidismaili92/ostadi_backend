

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from profils.models import Subject


SUBJECTS_LIST_URL = reverse('profils:subjects')

class TestSubjects(TestCase):
    """test operation on subjects (retrieve)"""

    def setUp(self):
        self.client = APIClient()
    def test_retrieve_subjects_list_success(self):
        #arrange
        payloadssubj1 = {
            "title":"test subject 1","icon":"test icon 1"
        }
        payloadssubj2 = {
            "title":"test subject 2","icon":"test icon 2"
        }
        first_subject = Subject.objects.create(**payloadssubj1)
        second_subject = Subject.objects.create(**payloadssubj2)
        
        #act
        res = self.client.get(SUBJECTS_LIST_URL)
        
        #assert
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual([item['title'] for item in res.data],[payloadssubj1['title'],payloadssubj2['title']])
            
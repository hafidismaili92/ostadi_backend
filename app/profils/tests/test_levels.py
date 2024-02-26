

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from profils.models import Level


LEVEL_LIST_URL = reverse('profils:levels')

class TestLevels(TestCase):
    """test operation on subjects (retrieve)"""

    def setUp(self):
        self.client = APIClient()
    def test_retrieve_levels_list_success(self):
        #arrange
        payloadslevel1 = {
            "title":"test level 1"
        }
        payloadslevel2 = {
            "title":"test level 2"
        }
        first_level = Level.objects.create(**payloadslevel1)
        second_level = Level.objects.create(**payloadslevel2)
        
        #act
        res = self.client.get(LEVEL_LIST_URL)
        
        #assert
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual([item['title'] for item in res.data],[first_level.title,second_level.title])
            
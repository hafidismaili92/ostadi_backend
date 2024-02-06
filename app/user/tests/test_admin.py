

from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class TestAdmin(TestCase):
    """test a superuser admin"""
    def setUp(self):
        self.userId=1
        self.client = Client()
        self.admin = get_user_model().objects.create_superuser(
        email ='test@example.com',
        password ='testpassword'
        )
        self.client.force_login(self.admin)
        self.simpleuser = get_user_model().objects.create_user(
        email ='testsimple@example.com',
        password ='testsimplepassword'
        )

    def test_get_user_list(self):
        #arrange
        url = reverse('admin:user_user_changelist')
        
        #act
        res = self.client.get(url)
        #assert
        
        self.assertContains(res,self.simpleuser.email)
        self.assertContains(res,self.simpleuser.name)
    
    def test_edit_user_page(self):
         #arrange
        url = reverse('admin:user_user_change',args=[self.userId])
        
        #act
        res = self.client.get(url)
        #assert
        
        self.assertEqual(res.status_code,200)
        
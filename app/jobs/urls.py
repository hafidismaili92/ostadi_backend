"""
Url Mappings for the JobPost API
"""

from django.urls import include, path
from jobs import views
from rest_framework import routers

app_name='jobs'


router = routers.DefaultRouter()
router.register(r'my-jobPosts', views.MyJobPostsViewSet, basename='my-jobPosts')
router.register(r'',views.AllJobPostsViewSet,basename='jobs')

urlpatterns = [
     path('', include(router.urls)),
   
]
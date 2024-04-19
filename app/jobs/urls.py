"""
Url Mappings for the JobPost API
"""

from django.urls import include, path
from jobs import views
from rest_framework import routers

app_name='jobs'


router = routers.DefaultRouter()
router.register(r'my-jobPosts', views.MyJobPostsViewSet, basename='my-jobPosts')
router.register(r'all-jobs',views.AllJobPostsViewSet,basename='jobs')

router.register(r'my-proposals',views.MyProposalsViewSet,basename='my-proposals')
urlpatterns = [
     path('', include(router.urls)),
   
]
"""
Url Mappings for the User API
"""

from django.urls import path
from profils import views

app_name='profils'

urlpatterns = [
    path('subjects/',views.SubjectsList.as_view(),name='subjects'),
    path('levels/',views.LevelsList.as_view(),name='levels'),
]
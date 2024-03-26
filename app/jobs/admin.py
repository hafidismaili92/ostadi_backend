from django.contrib import admin

from jobs.models import JobPost, Duration

admin.site.register(JobPost)
admin.site.register(Duration)
from django.contrib import admin

from jobs.models import JobPost, Duration, JobProposal

admin.site.register(JobPost)
admin.site.register(Duration)
admin.site.register(JobProposal)
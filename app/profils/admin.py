from django.contrib import admin

from profils.models import Level, Professor, Student, Subject

# Register your models here.

admin.site.register(Subject)
admin.site.register(Level)
admin.site.register(Student)
admin.site.register(Professor)
from django.contrib import admin
from .models import Task, Scheduler
# Register your models here.

admin.site.register(Task)
admin.site.register(Scheduler)
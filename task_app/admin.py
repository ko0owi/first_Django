from django.contrib import admin

# Register your models here.

from task_app.models import Task, Estate

admin.site.register(Task)
admin.site.register(Estate)

from django.contrib import admin
from django.contrib.admin.decorators import register

from quiz.models import Question, Response

admin.site.register(Question)
admin.site.register(Response) 
# Register your models here.

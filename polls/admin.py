from django.contrib import admin
from .models import Question, PollUser

admin.site.register(Question)
admin.site.register(PollUser)
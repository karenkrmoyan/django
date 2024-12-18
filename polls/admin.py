from django.contrib import admin
from .models import Question, PollUser, Choice

admin.site.register(Question)
admin.site.register(PollUser)
admin.site.register(Choice)
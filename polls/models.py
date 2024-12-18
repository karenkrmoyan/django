import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class PollUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50)


class Question(models.Model):
    author = models.ForeignKey(PollUser, on_delete=models.CASCADE, null=True, blank=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("publication date")

    def __str__(self):
        return "{} | {}".format(self.id, self.question_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} | {} - {}".format(self.id, self.choice_text, self.votes)



class UserLog(models.Model):
    actions = [
        ("login", "Login Successfully"),
        ("question", "Look question list"),
        ("vote", "Vote a question"),
        ("detail", "View single question info"),
        ("choice+", "Adding a choice to a question"),
        ("question+", "Adding a new question")
    ]

    user = models.ForeignKey(PollUser, on_delete=models.CASCADE)
    action_time = models.DateField()
    action = models.CharField(max_length=20, choices=actions)

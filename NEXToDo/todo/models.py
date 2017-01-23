import datetime

from django.db import models
from django.utils import timezone


class Todo(models.Model):
    question_text = models.CharField('Todo',max_length=200)
    pub_date = models.DateTimeField('締め切り')

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
"""
class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
"""

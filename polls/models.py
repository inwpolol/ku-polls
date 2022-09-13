import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """
    Create model of Question that consist of question text, publication date
    and ending date.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('end date', null=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        now = timezone.now()
        return now >= self.pub_date

    def can_vote(self):
        now = timezone.now()
        if self.end_date:
            return self.end_date + datetime.timedelta(seconds=1) >= now >= self.pub_date
        return self.is_published()
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    """
    Create model of Choice that consist of choice text and a vote tally. 
    Each Choice is associated with a Question.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
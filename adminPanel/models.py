from django.db import models
from django.contrib.auth.models import User
# import datetime
from datetime import datetime
# Create your models here.
class Test(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subjectName = models.CharField(max_length=200)
    totalQuestions = models.IntegerField()
    totalMarks = models.IntegerField()
    dateTime = models.CharField(max_length=100)
    examDuration = models.IntegerField()
    negativeMarksInput = models.IntegerField()
    createdOn = models.DateField(("Posted on"), default=datetime.now())

    def __str__(self):
        return self.subjectName

class Question(models.Model):
    subject = models.ForeignKey(Test,on_delete=models.CASCADE,null=True)
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    difficulty_level = models.IntegerField(default=1)

    def __str__(self):
        return self.question


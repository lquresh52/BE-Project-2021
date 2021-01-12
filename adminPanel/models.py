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
    dateTime = models.DateTimeField(max_length=100)
    examDuration = models.IntegerField()
    # negativeMarksInput = models.IntegerField()
    createdOn = models.DateTimeField(auto_now_add=True)
    quiz_completed = models.BooleanField(default=False)
    number_of_question_added = models.IntegerField(default=0)
    # createdOn = models.DateField(("Posted on"), default=datetime.now())
    class Meta:
        ordering = ['-createdOn',]

    def __str__(self):
        return self.subjectName

class Question(models.Model):
    subject = models.ForeignKey(Test,on_delete=models.CASCADE,null=True)
    question_number = models.IntegerField()
    question = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    answer = models.IntegerField()
    # difficulty_level = models.IntegerField(default=1)
    

    def __str__(self):
        return self.question


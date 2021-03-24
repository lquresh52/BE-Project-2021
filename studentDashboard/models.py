from django.db import models 
from django.contrib.auth.models import User
from adminPanel.models import Test
import jsonfield

# Create your models here.
class Time_Tracker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE,null=True)
    time_left = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.test_id)
        

class Exam_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE,null=True)
    score = models.IntegerField()
    no_of_que = models.IntegerField()
    right_ans = models.IntegerField()
    wrong = models.IntegerField()
    selected_ans = jsonfield.JSONField()
    is_test_given = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return f'{self.user.first_name} - Quiz id: {self.test_id} - Score : {self.score}'
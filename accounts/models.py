from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    isTeacher = models.BooleanField(default=False)
    college_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=100, null=True)
    year = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


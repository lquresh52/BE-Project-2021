from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    # college_name = models.CharField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


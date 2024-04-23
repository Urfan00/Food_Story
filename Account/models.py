from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    bio = models.TextField('Bio', null=True, blank=True)
    image = models.ImageField(upload_to = 'users_avatars', null=True, blank=True)
    phonenumber = models.CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

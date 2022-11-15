from django.db import models
from django.contrib.auth.models import AbstractUser  # AbstractUser by default doesn't have email status description fields (different from AbstractBaseUser)


# Create your models here.
class CustomUser(AbstractUser):

    STATUS = (  # addition to understand better

        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator')  # ADMIN

    )

    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='regular')
    description = models.TextField('Description', max_length=600, default='', blank=True)

    def __str__(self):

        return self.username

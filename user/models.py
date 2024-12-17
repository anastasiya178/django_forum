from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.
# Overwriting standard User to use email address for login

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'



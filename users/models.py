from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Roles(models.TextChoices):
        USER = 'user', _('USER')
        MODERATOR = 'moderator', _('MODERATOR')
        ADMIN = 'admin', _('ADMIN')
    
    email = models.EmailField(blank=False, unique=True)
    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.USER
    )
    bio = models.CharField(max_length=30, blank=True)
    REQUIRED_FIELDS = ('email',)

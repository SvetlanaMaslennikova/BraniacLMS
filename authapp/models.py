from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(blank=True, verbose_name=_('Email'), unique=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name=_('Age'))
    avatar = models.ImageField(upload_to='users', blank=True, null=True, verbose_name=_('Avatar'))

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

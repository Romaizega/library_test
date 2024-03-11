from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.constants import (MAX_EMAIL_LENGTH, MAX_FIELD_LENGTH,
                             MAX_PHONE_NUMBER_LENGTH)


class User(AbstractUser):
    """Модель пользователей."""

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        unique=True,
        verbose_name='Адрес электронной почты')

    username = models.CharField(
        unique=True,
        max_length=MAX_FIELD_LENGTH,
        verbose_name='Имя пользователя',
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message=('Username может содержать только буквы, '
                         'цифры и  @/./+/-/_..')
            )
        ],
    )
    first_name = models.CharField(
        max_length=MAX_FIELD_LENGTH,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=MAX_FIELD_LENGTH,
        verbose_name='Фамилия'
    )
    phone_number = PhoneNumberField(
        max_length=MAX_PHONE_NUMBER_LENGTH,
        default=''
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from community.models import Organisation
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
        default='',
        verbose_name='Номер телефона'
    )
    organizations = models.ManyToManyField(
        Organisation,
        related_name='users',
        verbose_name='Организации',
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return self.username


class UserOrganisation(models.Model):
    """Модель пользователя-организации."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    organisation = models.ForeignKey(
        Organisation,
        on_delete=models.CASCADE,
        verbose_name='Организация'
    )

    class Meta:
        verbose_name = 'Пользователь-организация'
        verbose_name_plural = 'Пользователи-организации'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'organisation'],
                name='unique_user_organisation'
            ),
            models.CheckConstraint(
                name='ban_user_from_organisation',
                check=~models.Q(user=models.F('organisation')),
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.organisation}'

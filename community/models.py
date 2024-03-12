from django.core.validators import RegexValidator
from django.db import models

from community.constants import (MAX_CHAR_FIELD_LENGTH,
                                 MAX_CHAR_FIELD_POSTCODE_LENGTH)


class Organisation(models.Model):
    title = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH,
        verbose_name='Название организации'
    )
    description = models.TextField(
        verbose_name='Описание организации'
    )
    address = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH,
        verbose_name='Адрес организации',
        help_text='Введите полный адрес организации'
    )
    postcode = models.CharField(
        max_length=MAX_CHAR_FIELD_POSTCODE_LENGTH,
        verbose_name='Почтовый индекс',
        validators=[
            RegexValidator(
                regex=r'^\d{6}$',
                message='Почтовый индекс должен содержать 6 цифр')
        ]
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(
        max_length=MAX_CHAR_FIELD_LENGTH,
        verbose_name='Название мероприятия'
    )
    description = models.TextField(
        verbose_name='Описание мероприятия'
    )
    organizations = models.ManyToManyField(
        Organisation,
        verbose_name='Организаторы мероприятия'
    )
    image = models.ImageField(
        upload_to='events/images/',
        verbose_name='Фотография мероприятия',
        blank=True,
        null=True
    )
    date = models.DateField(
        verbose_name='Дата проведения мероприятия'
    )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'
        ordering = ('-date',)

    def __str__(self):
        return self.title

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    TYPE_CHOICES = (
        ('company', 'Предприятие'),
        ('physical_person', 'Физ. лицо'),
    )

    surname = models.CharField(max_length=100, verbose_name="Отчество")
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, verbose_name="Тип пользователя")
    region = models.CharField(max_length=100, verbose_name="Регион")
    city = models.CharField(max_length=100, verbose_name="Город")
    company_name = models.CharField(max_length=100, verbose_name="Наименование предприятия")
    inn = models.CharField(max_length=100, verbose_name="ИНН")
    place_orders = models.BooleanField(default=False, verbose_name="Для размещения заказов")
    responses_orders = models.BooleanField(default=False, verbose_name="Для откликов на заказы")
    another_goal = models.BooleanField(default=False, verbose_name="Другая цель")
    number_phone = models.CharField(max_length=100, verbose_name="Номер телефона")
    newsletter = models.BooleanField(default=False, verbose_name="Новостная рассылка")
    new_order_alerts = models.BooleanField(default=False, verbose_name="Оповещения о новых заказах")

    def __str__(self):
        return self.username


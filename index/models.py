from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser

class Production_categories(models.Model):
    title = models.CharField(max_length=100, verbose_name="Категории предприятий")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория предприятий'
        verbose_name_plural = 'Категории предприятий'

class Company(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Наименование предприятия")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, verbose_name="Описание")
    legal_address = models.CharField(max_length=100, verbose_name="Юридический адрес")
    number_phone = models.CharField(max_length=100, verbose_name="Номер телефона")
    email = models.CharField(max_length=100, verbose_name="E-mail")
    production_categories = models.ManyToManyField('Production_categories', verbose_name="Категории предприятия")
    image = models.ImageField(upload_to='images/', verbose_name="Логотип")

    def __str__(self):
        return f"{self.company_name} ({self.user.username})"

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Advantages(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    advert = models.ForeignKey('Advert', on_delete=models.CASCADE, verbose_name="Тариф")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

class Advert(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    price = models.IntegerField(verbose_name="Стоимость")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'



class Advertisement(models.Model):
    title = models.CharField(max_length=250, verbose_name="Загаловок")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    categories = models.ForeignKey(Production_categories, on_delete=models.CASCADE, verbose_name="Категория")
    description = models.CharField(max_length=250, verbose_name="Описание")
    img = models.ImageField(upload_to='images/', verbose_name="Изображение", null=True)
    price = models.IntegerField(verbose_name="Стоимость")
    currency = models.CharField(max_length=250, verbose_name="Валюта")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    contact_person = models.CharField(max_length=250, verbose_name="Контактное лицо")
    number_phone = models.CharField(max_length=250, verbose_name="Номер телефона")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

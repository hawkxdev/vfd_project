from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=30, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class EquipmentLine(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Линейка оборудования'
        verbose_name_plural = 'Линейки оборудования'


class Supplier(models.Model):
    name = models.CharField('Наименование', max_length=50, unique=True)
    site = models.CharField('Сайт', max_length=100)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT)
    CURRENCY_CHOICES = (
        ('BYN', 'BYN'),
        ('RUB', 'RUB'),
        ('EUR', 'EUR'),
        ('USD', 'USD'),
    )
    currency = models.CharField('Валюта', max_length=3, choices=CURRENCY_CHOICES)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ('id',)


class Brand(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)
    site = models.CharField('Сайт', max_length=150)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT)
    equipment_lines = models.ManyToManyField(EquipmentLine, verbose_name='Линейки оборудования')
    description = models.TextField('Описание', null=True, blank=True)
    suppliers = models.ManyToManyField(Supplier, verbose_name='Поставщики')
    logo = models.ImageField('Логотип', upload_to='logos/')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

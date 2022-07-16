from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class EquipmentLine(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Линейка оборудования'
        verbose_name_plural = 'Линейки оборудования'


class Supplier(models.Model):
    name = models.CharField('Наименование', max_length=200, unique=True)
    site = models.CharField('Сайт', max_length=150)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT)
    CURRENCY_CHOICES = (
        ('BYN', 'BYN'),
        ('RUB', 'RUB'),
        ('EUR', 'EUR'),
        ('USD', 'USD'),
    )
    currency = models.CharField('Валюта', max_length=200, choices=CURRENCY_CHOICES)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Brand(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)
    site = models.CharField('Сайт', max_length=150)
    country = models.ForeignKey(Country, verbose_name='Страна', on_delete=models.PROTECT)
    equipment_lines = models.ManyToManyField(EquipmentLine, verbose_name='Линейки оборудования')
    description = models.TextField('Описание')
    suppliers = models.ManyToManyField(Supplier, verbose_name='Поставщики')
    logo = models.ImageField('Логотип', upload_to='logos/')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Application(models.Model):
    name = models.CharField('Наименование', max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Применение'
        verbose_name_plural = 'Применения'


class Category(models.Model):
    name = models.CharField('Наименование', max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Series(models.Model):
    name = models.CharField('Название', max_length=200, unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.PROTECT)
    applications = models.ManyToManyField(Application, verbose_name='Применения')
    power_min = models.FloatField(verbose_name='Мощность, от')
    power_max = models.FloatField(verbose_name='Мощность, до')
    overload_capacity = models.CharField('Перегрузочная способность', max_length=200)
    digital_inputs = models.IntegerField(verbose_name='Дискретные входы')
    analog_inputs = models.IntegerField(verbose_name='Аналоговые входы')
    transistor_outputs = models.IntegerField(verbose_name='Транзисторные выходы')
    relay_outputs = models.IntegerField(verbose_name='Релейные выходы')
    analog_outputs = models.IntegerField(verbose_name='Аналоговые выходы')
    control_panel = models.CharField('Панель управления', max_length=200)
    control_panel_included = models.BooleanField('Панель управления в комплекте')
    COMMUNICATION_CHOICES = (
        ('No', 'Нет'),
        ('ModBusRTU', 'RS-485 Modbus RTU'),
    )
    built_in_communication = models.CharField('Встроенный протокол связи', max_length=200,
                                              choices=COMMUNICATION_CHOICES)
    ADD_COMMUNICATION_CHOICES = (
        ('No', 'Нет'),
        ('Expansion cards', 'Да, платы расширения'),
        ('ModBusRTU', 'RS-485 Modbus RTU'),
        ('CANopen', 'CANopen'),
    )
    additional_communications = models.CharField('Дополнительные протоколы связи', max_length=200,
                                                 choices=ADD_COMMUNICATION_CHOICES)
    EMC_FILTER_CHOICES = (
        ('No', 'Нет'),
        ('C3', 'C3'),
        ('C2', 'C2'),
        ('No_C2', 'Нет/C2'),
    )
    emc_filter = models.CharField(verbose_name='Встроенный EMC фильтр', max_length=10, choices=EMC_FILTER_CHOICES)
    choke_dc_link = models.CharField(verbose_name='Дроссель в звене постоянного тока', max_length=300)
    brake_interrupter = models.CharField(verbose_name='Тормозной прерыватель', max_length=300)
    PLC_CHOICES = (
        ('No', 'Нет'),
        ('Yes', 'Да'),
        ('mini-PLC', 'mini-PLC'),
        ('SequenceProgramming', 'Программирование последовательности'),
    )
    built_in_plc = models.CharField(verbose_name='Встроенный ПЛК', max_length=200, choices=PLC_CHOICES)
    PROTECTION_CHOICES = (
        ('IP20', 'IP20'),
        ('IP21', 'IP21'),
        ('IP55', 'IP55'),
    )
    protection_degree = models.CharField(verbose_name='Степень защиты', max_length=200, choices=PROTECTION_CHOICES)
    TEMP_CHOICES = (
        ('-10...+40', '-10...+40'),
        ('-10...+50', '-10...+50'),
        ('-15...+50', '-15...+50'),
        ('-20...+50', '-20...+50'),
    )
    operating_temp = models.CharField(verbose_name='Рабочая температура', max_length=200, choices=TEMP_CHOICES)
    description = models.TextField('Описание')
    image = models.ImageField('Картинка', upload_to='images/')

    def __str__(self):
        return str(f'{self.brand} {self.name}')

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'
        ordering = ('brand', 'name')


class FrequencyDrive(models.Model):
    article = models.CharField('Артикул', max_length=30, unique=True)
    name = models.CharField('Наименование', max_length=200, blank=True, null=True)
    series = models.ForeignKey(Series, verbose_name='Серия', on_delete=models.PROTECT, blank=False, null=False)
    POWER_CHOICES = (
        (2.2, '2.2'),
        (7.5, '7.5'),
        (22, 22),
        (45, 45),
        (110, 110),
        (250, 250),
    )
    power = models.FloatField('Мощность', choices=POWER_CHOICES)
    current = models.FloatField('Ток')
    VOLT_CHOICES = (
        (380, 380),
        (220, 220),
    )
    voltage = models.FloatField('Напряжение', default=380, choices=VOLT_CHOICES)

    def __str__(self):
        return str(f'{self.series.brand} | {self.article} | {self.power}kW')

    class Meta:
        verbose_name = 'Частотник'
        verbose_name_plural = 'Частотники'
        ordering = ('series__brand', 'article')


class AccessoryType(models.Model):
    name = models.CharField('Наименование', max_length=200, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Тип аксессуара'
        verbose_name_plural = 'Тип аксессуаров'


class Accessory(models.Model):
    article = models.CharField('Артикул', max_length=30, unique=True)
    name = models.CharField('Наименование', max_length=200, blank=True, null=True)
    type = models.ForeignKey(AccessoryType, verbose_name='Тип аксессуара', on_delete=models.PROTECT)
    series = models.ManyToManyField(Series, verbose_name='Серии')

    def __str__(self):
        return str(f'{self.series.brand} | {self.article} | {self.name}')

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'
        ordering = ('series__brand', 'article')


class Price(models.Model):
    frequency_drive = models.ForeignKey(FrequencyDrive, verbose_name='Частотник', on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', on_delete=models.PROTECT)
    price = models.FloatField('Цена')

    def __str__(self):
        return str(f'{self.frequency_drive.article} | {self.price} {self.supplier.currency} | {self.supplier.name}')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

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
        ordering = ('name',)


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
    overload_capacity = models.TextField('Перегрузочная способность', blank=True, null=True)

    control_methods = models.CharField(verbose_name='Методы управления', max_length=200, blank=True, null=True)
    starting_torque = models.CharField('Пусковой момент', max_length=200, blank=True, null=True)
    setting_vf_characteristic = models.CharField('Задание характеристики V/F', max_length=200, blank=True, null=True)
    speed_control_range = models.FloatField(verbose_name='Диапазон регулирования скорости, Гц', blank=True, null=True)
    torque_limitation = models.CharField('Ограничение момента', max_length=200, blank=True, null=True)
    torque_accuracy = models.CharField('Точность по моменту', max_length=20, blank=True, null=True)
    maximum_output_frequency = models.CharField(verbose_name='Максимальная выходная частота',
                                                max_length=200, blank=True, null=True)
    output_frequency_accuracy = models.CharField('Точность выходной частоты', max_length=200, blank=True, null=True)
    frequency_set_discreteness = models.CharField('Дискретность задания частоты', max_length=200, blank=True, null=True)
    frequency_set_signals = models.CharField('Сигналы задания частоты', max_length=200, blank=True, null=True)
    acceleration_deceleration_time = models.CharField('Время разгона/торможения', max_length=200, blank=True, null=True)
    main_control_functions = models.TextField('Основные функции управления', blank=True, null=True)
    control_built_in_fan = models.CharField('Управление встроенным вентилятором охлаждения',
                                            max_length=200, blank=True, null=True)
    engine_protection = models.CharField('Защита двигателя', max_length=200, blank=True, null=True)
    overcurrent_protection = models.TextField('Защита от перегрузки по току', blank=True, null=True)
    overvoltage_protection = models.CharField('Защита по превышению напряжения', max_length=200, blank=True, null=True)
    temperature_protection = models.CharField('Защита по температуре', max_length=200, blank=True, null=True)
    stop_prevention = models.CharField('Предотвращение остановки', max_length=200, blank=True, null=True)
    automatic_start_after_power_loss = models.CharField('Автоматический запуск после пропадания питания',
                                                        max_length=200, blank=True, null=True)
    current_leakage_protection = models.CharField('Защита от утечек тока на землю',
                                                  max_length=200, blank=True, null=True)

    digital_inputs = models.IntegerField(verbose_name='Дискретные входы', blank=True, null=True)
    analog_inputs = models.IntegerField(verbose_name='Аналоговые входы', blank=True, null=True)
    transistor_outputs = models.IntegerField(verbose_name='Транзисторные выходы', blank=True, null=True)
    relay_outputs = models.IntegerField(verbose_name='Релейные выходы', blank=True, null=True)
    analog_outputs = models.IntegerField(verbose_name='Аналоговые выходы', blank=True, null=True)
    control_panel = models.TextField('Панель управления', blank=True, null=True)
    control_panel_included = models.BooleanField('Панель управления в комплекте', blank=True, null=True)
    control_panel_at_distance = models.CharField('Возможность выносного крепления панели',
                                                 max_length=200, blank=True, null=True)
    COMMUNICATION_CHOICES = (
        ('No', 'Нет'),
        ('ModBusRTU', 'Modbus RTU'),
        ('ModBusRTU/BACnet', 'Modbus RTU, BACnet'),
    )
    built_in_communication = models.CharField('Встроенный протокол связи', max_length=200,
                                              choices=COMMUNICATION_CHOICES, blank=True, null=True)
    additional_communications = models.CharField('Дополнительные протоколы связи',
                                                 max_length=200, blank=True, null=True)
    EMC_FILTER_CHOICES = (
        ('No', 'Нет'),
        ('C3', 'C3'),
        ('C2', 'C2'),
        ('No_C2', 'Нет/C2'),
    )
    emc_filter = models.CharField(verbose_name='Встроенный EMC фильтр', max_length=10, choices=EMC_FILTER_CHOICES
                                  , blank=True, null=True)
    choke_dc_link = models.CharField(verbose_name='Дроссель в звене постоянного тока', max_length=300
                                     , blank=True, null=True)
    brake_interrupter = models.CharField(verbose_name='Тормозной прерыватель', max_length=300
                                         , blank=True, null=True)
    built_in_plc = models.CharField(verbose_name='Встроенный ПЛК', max_length=200, blank=True, null=True)

    installation_place = models.CharField(verbose_name='Место установки', max_length=200, blank=True, null=True)
    operating_temp = models.TextField(verbose_name='Рабочая температура, ℃', blank=True, null=True)
    storage_temp = models.CharField(verbose_name='Температура хранения, ℃', max_length=200, blank=True, null=True)
    transport_temp = models.CharField(verbose_name='Температура транспортировки, ℃',
                                      max_length=200, blank=True, null=True)
    use_relative_humidity = models.CharField(verbose_name='Относительная влажность при эксплуатации',
                                             max_length=200, blank=True, null=True)
    storage_transportation_relative_humidity = models.CharField(
        verbose_name='Относительная влажность при хранении/транспортировке', max_length=200, blank=True, null=True)
    atmospheric_pressure_use_storage = models.CharField(
        verbose_name='Атмосферное давление при эксплуатации/хранении, кПа', max_length=200, blank=True, null=True)
    atmospheric_pressure_transportation = models.CharField(
        verbose_name='Атмосферное давление при транспортировке, кПа', max_length=200, blank=True, null=True)
    pollution_level_use = models.CharField(verbose_name='Уровень загрязнения при эксплуатации',
                                           max_length=200, blank=True, null=True)
    pollution_level_storage = models.CharField(verbose_name='Уровень загрязнения при хранении',
                                               max_length=200, blank=True, null=True)
    pollution_level_transportation = models.CharField(verbose_name='Уровень загрязнения при транспортировке',
                                                      max_length=200, blank=True, null=True)
    installation_altitude = models.TextField(verbose_name='Высота установки', blank=True, null=True)
    vibration = models.TextField(verbose_name='Вибрация', blank=True, null=True)
    impact_resistance = models.TextField(verbose_name='Ударопрочность', blank=True, null=True)
    mounting_position = models.CharField(verbose_name='Положение монтажа', max_length=200, blank=True, null=True)
    wall_to_wall_installation = models.CharField(verbose_name='Монтаж "Стенка к стенке"',
                                                 max_length=200, blank=True, null=True)

    PROTECTION_CHOICES = (
        ('IP20', 'IP20'),
        ('IP21', 'IP21'),
        ('IP55', 'IP55'),
    )
    protection_degree = models.CharField(verbose_name='Степень защиты', max_length=200, choices=PROTECTION_CHOICES
                                         , blank=True, null=True)

    motor_cable_length = models.TextField(verbose_name='Максимальная длина кабеля двигателя', blank=True, null=True)
    encoder_support = models.BooleanField(verbose_name='Подключение энкодера', blank=True, null=True)
    pre_configurations = models.CharField(verbose_name='Предварительные конфигурации',
                                          max_length=200, blank=True, null=True)
    copy_backup_settings = models.BooleanField(verbose_name='Возможность копирования/бэкапа настроек'
                                               , blank=True, null=True)
    engine_cascade_control = models.CharField(verbose_name='Управление каскадом двигателей',
                                              max_length=200, blank=True, null=True)
    multi_pump_system = models.CharField(
        verbose_name='Система Multi-pump (группа приводов-насосов подключенных по шине)',
        max_length=200, blank=True, null=True)
    pid_controller = models.IntegerField(verbose_name='Встроенный ПИД-регулятор', blank=True, null=True)
    fire_mode = models.BooleanField(verbose_name='Пожарный режим', blank=True, null=True)
    circuit_boards_protection = models.CharField(verbose_name='Защита печатных плат',
                                                 max_length=200, blank=True, null=True)
    sleep_mode = models.BooleanField(verbose_name='Спящий режим', blank=True, null=True)
    flying_start = models.BooleanField(verbose_name='Подхват на ходу', blank=True, null=True)
    skip_frequency = models.BooleanField(verbose_name='Пропуск критических частот', blank=True, null=True)
    realtime_clock = models.BooleanField(verbose_name='Часы реального времени', blank=True, null=True)
    quick_change_fans = models.BooleanField(verbose_name='Быстросъёмные вентиляторы', blank=True, null=True)
    automatic_energy_saving = models.BooleanField(verbose_name='Автоматическое энергосбережение', blank=True, null=True)
    io_expansion_boards = models.BooleanField(verbose_name='Платы расширения входов-выходов', blank=True, null=True)
    removable_terminal_blocks = models.BooleanField(verbose_name='Съёмные клеммные колодки', blank=True, null=True)
    dual_circuit_cooling = models.BooleanField(verbose_name='Двухконтурное охлаждение', blank=True, null=True)
    sto_function = models.BooleanField(verbose_name='Функция STO (безопасного отключения момента)',
                                       blank=True, null=True)

    description = models.TextField('Описание', blank=True, null=True)
    image = models.ImageField('Картинка', upload_to='images/', blank=True, null=True)

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
        (400, 400),
        (230, 230),
    )
    voltage = models.FloatField('Напряжение', default=380, choices=VOLT_CHOICES)

    def __str__(self):
        return str(f'{self.series.brand} | {self.series.name} | {self.article} | {self.power}kW')

    class Meta:
        verbose_name = 'Частотник'
        verbose_name_plural = 'Частотники'
        ordering = ('series__brand', 'series__name', 'voltage', 'power')


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
        return str(f'{self.series.first().brand} | {self.article} | {self.name}')

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'
        ordering = ('series__brand', 'article')


class Price(models.Model):
    frequency_drive = models.ForeignKey(FrequencyDrive, verbose_name='Частотник', on_delete=models.PROTECT,
                                        blank=True, null=True)
    accessory = models.ForeignKey(Accessory, verbose_name='Аксессуар', on_delete=models.PROTECT, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', on_delete=models.PROTECT)
    price = models.FloatField('Цена')

    def __str__(self):
        return str(f'{self.frequency_drive.article} | {self.price} {self.supplier.currency} | {self.supplier.name}')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

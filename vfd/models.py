from django.db import models
from supplier.models import Country, EquipmentLine, Supplier, Brand


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
    brand = models.ForeignKey(Brand, verbose_name='Бренд', on_delete=models.PROTECT)
    name = models.CharField('Название', max_length=200, unique=True)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)
    image = models.ImageField('Картинка', upload_to='images/', blank=True, null=True)
    applications = models.ManyToManyField(Application, verbose_name='Применения')

    class Power(models.IntegerChoices):
        P1 = 1, '1x220В: 0.4...2.2кВт; 3x380В: 0.75...3.7кВт'
        P2 = 2, '1x220В: 0.2...2.2кВт; 3x380В: 0.4...22кВт'
        P3 = 3, '0.75...500кВт'

    power_range = models.PositiveSmallIntegerField(verbose_name='Диапазон мощностей',
                                                   choices=Power.choices, blank=True, null=True)

    class ControlMethods(models.IntegerChoices):
        C10 = 10, 'V/F (скалярное управление), \nSVC (бездатчиковое векторное управление)'
        C11 = 11, 'V/F (скалярное управление), \nFVC (векторное управление потоком)'

    control_methods = models.PositiveSmallIntegerField(verbose_name='Методы управления',
                                                       choices=ControlMethods.choices, blank=True, null=True)

    class Motors(models.IntegerChoices):
        F1 = 1, 'IM (асинхронные)'
        F2 = 2, 'IM (асинхронные), PM (синхронные с постоянными магнитами)'
        F3 = 3, 'IM (асинхронные), PM (синхронные с постоянными магнитами), SynRM (синхронные реактивные)'

    motors = models.PositiveSmallIntegerField(verbose_name='Двигатели', choices=Motors.choices, blank=True, null=True)

    class MaximumFrequency(models.IntegerChoices):
        F1 = 1, '320'
        F2 = 2, '599 Гц; 90 кВт и выше: 400 Гц'
        F3 = 3, '599'

    maximum_output_frequency = models.PositiveSmallIntegerField(verbose_name='Максимальная выходная частота, Гц',
                                                                choices=MaximumFrequency.choices, blank=True, null=True)

    class Overload(models.IntegerChoices):
        P1 = 1, 'Лёгкий режим: 120% 60с; \nНормальный режим: 120% 60с, 160% 3с'
        P2 = 2, '150% 60s; 180% 3s'
        P3 = 3, 'Нормальный режим: 120% 60с, 150% 3с; \nТяжелый режим: 150% 60с, 200% 3с'

    overload_capacity = models.PositiveSmallIntegerField('Перегрузочная способность',
                                                         choices=Overload.choices, blank=True, null=True)

    class StartingTorque(models.IntegerChoices):
        S1 = 1, '150% / 3 Гц'
        S2 = 2, '160% / 0.5 Гц'

    starting_torque = models.PositiveSmallIntegerField('Пусковой момент (V/F)', choices=StartingTorque.choices,
                                                       blank=True, null=True)

    class MultiPump(models.IntegerChoices):
        W1 = 1, 'Нет'
        W2 = 2, 'Да, до 4 насосов'
        W3 = 3, 'Да, до 8 насосов'

    multi_pump_system = models.PositiveSmallIntegerField(verbose_name='Много-насосный режим',
                                                         choices=MultiPump.choices, blank=True, null=True)

    class Cascade(models.IntegerChoices):
        C1 = 1, 'Нет'
        C2 = 2, 'Да, до 4 двигателей'
        C3 = 3, 'Да, до 8 двигателей'

    engine_cascade_control = models.PositiveSmallIntegerField(verbose_name='Управление каскадом двигателей',
                                                              choices=Cascade.choices, blank=True, null=True)

    class DifferentEngines(models.IntegerChoices):
        D0 = 0, 'Нет'
        D1 = 1, 'До 4 независимых групп параметров двигателя'

    different_engines_work = models.PositiveSmallIntegerField(verbose_name='Работа с разными двигателями',
                                                              choices=DifferentEngines.choices, blank=True, null=True)

    fire_mode = models.BooleanField(verbose_name='Пожарный режим', blank=True, null=True)
    sleep_mode = models.BooleanField(verbose_name='Спящий режим', blank=True, null=True)
    flying_start = models.BooleanField(verbose_name='Подхват на ходу', blank=True, null=True)
    skip_frequency = models.BooleanField(verbose_name='Пропуск критических частот', blank=True, null=True)
    automatic_energy_saving = models.BooleanField(verbose_name='Автоматическое энергосбережение', blank=True, null=True)

    class EngineProtection(models.IntegerChoices):
        P1 = 1, 'Перегрузка по току, перенапряжение, перегрев, потеря фазы'

    engine_protection = models.PositiveSmallIntegerField('Защита двигателя', choices=EngineProtection.choices,
                                                         blank=True, null=True)

    class StopPrevention(models.IntegerChoices):
        P1 = 1, 'Токоограничение при разгоне, замедлении и работе (общая настройка)'
        P2 = 2, 'Токоограничение при разгоне, замедлении и работе (независимые настройки)'

    stop_prevention = models.PositiveSmallIntegerField('Предотвращение перегрузки',
                                                       choices=StopPrevention.choices, blank=True, null=True)

    automatic_start_after_power_loss = models.BooleanField('Преодоление провалов напряжения питания',
                                                           blank=True, null=True)

    class InputsOutputs(models.IntegerChoices):
        IO1 = 1, 'DI: 4; AI: 2; TO: 0; RO: 1; AO: 1'
        IO2 = 2, 'DI: 7; AI: 2; TO: 3; RO: 1; AO: 1'
        IO3 = 3, 'DI: 10; AI: 3; TO: 0; RO: 3; AO: 2'

    inputs_outputs = models.PositiveSmallIntegerField(verbose_name='Входы/выходы',
                                                      choices=InputsOutputs.choices, blank=True, null=True)

    io_expansion_boards = models.BooleanField(verbose_name='Платы расширения входов-выходов', blank=True, null=True)
    pulse_frequency_setting = models.BooleanField('Импульсное задание частоты', blank=True, null=True)

    class ControlPanel(models.IntegerChoices):
        P1 = 1, 'Светодиодная 4-символьная'
        P2 = 2, 'Светодиодная 5-символьная'
        P3 = 3, 'ЖК-дисплей'

    control_panel = models.PositiveSmallIntegerField('Панель управления', choices=ControlPanel.choices,
                                                     blank=True, null=True)

    control_panel_desc = models.TextField('Описание панели управления', blank=True, null=True)
    control_panel_included = models.BooleanField('Панель управления в комплекте', blank=True, null=True)

    class PanelAtDistance(models.IntegerChoices):
        P0 = 0, 'Нет'
        P1 = 1, 'Да, при помощи кабеля-аксессуара'
        P2 = 2, 'Да, соединение обычным патч-кордом'

    control_panel_at_distance = models.PositiveSmallIntegerField('Выносной пульт',
                                                                 choices=PanelAtDistance.choices, blank=True, null=True)

    class Configurations(models.IntegerChoices):
        C1 = 1, 'Группировка параметров по применениям'

    pre_configurations = models.PositiveSmallIntegerField(verbose_name='Предварительные конфигурации (Макросы)',
                                                          choices=Configurations.choices, blank=True, null=True)

    copy_backup_settings = models.BooleanField(verbose_name='Копирование/бэкап настроек', blank=True, null=True)
    pid_controller = models.IntegerField(verbose_name='Встроенный ПИД-регулятор', blank=True, null=True)

    class Communications(models.IntegerChoices):
        C0 = 0, 'Нет'
        C1 = 1, 'Modbus RTU'
        C2 = 2, 'Modbus RTU, BACnet'

    built_in_communication = models.PositiveSmallIntegerField('Встроенный протокол связи',
                                                              choices=Communications.choices, blank=True, null=True)

    class AdditionalCommunications(models.IntegerChoices):
        C0 = 0, 'Нет'
        C1 = 1, 'DeviceNet, Ethernet IP, Modbus TCP, CANopen, Profibus DP'

    additional_communications = models.PositiveSmallIntegerField('Дополнительные протоколы связи',
                                                                 choices=AdditionalCommunications.choices,
                                                                 blank=True, null=True)

    class Plc(models.IntegerChoices):
        PO = 0, 'Нет'
        P2 = 2, 'ПЛК на 2000 шагов'
        P3 = 3, 'ПЛК на 10000 шагов'

    built_in_plc = models.PositiveSmallIntegerField(verbose_name='Встроенный ПЛК',
                                                    choices=Plc.choices, blank=True, null=True)

    encoder_support = models.BooleanField(verbose_name='Подключение энкодера', blank=True, null=True)
    sto_function = models.BooleanField(verbose_name='Стандарт безопасности STO', blank=True, null=True)

    class ExternalPower(models.IntegerChoices):
        P1 = 0, 'Нет'
        P2 = 1, 'Опциональная плата'

    external_power_24v = models.PositiveSmallIntegerField(verbose_name='Подключение внешнего питания +24В',
                                                          choices=ExternalPower.choices, blank=True, null=True)

    class Usb(models.IntegerChoices):
        U0 = 0, 'Нет'
        U1 = 1, 'Есть (загрузка и выгрузка даже без включения питания)'

    built_in_usb = models.PositiveSmallIntegerField(verbose_name='Встроенный порт USB',
                                                    choices=Usb.choices, blank=True, null=True)

    class EmcFilter(models.IntegerChoices):
        NO = 0, 'Нет'
        C3 = 1, 'C3'
        C2 = 2, 'C2'

    emc_filter = models.PositiveSmallIntegerField(verbose_name='Встроенный EMC фильтр',
                                                  choices=EmcFilter.choices, blank=True, null=True)

    class ChokeDc(models.IntegerChoices):
        C0 = 0, 'Нет'
        C1 = 1, 'Опция'
        C2 = 2, 'Встроен на мощности от 45 кВт'

    choke_dc_link = models.PositiveSmallIntegerField(verbose_name='Дроссель в звене постоянного тока',
                                                     choices=ChokeDc.choices, blank=True, null=True)

    class BrakeInterrupter(models.IntegerChoices):
        C0 = 0, 'Нет'
        C1 = 1, 'Встроен на мощности до 37 кВт'
        C2 = 2, 'Встроен'

    brake_interrupter = models.PositiveSmallIntegerField(verbose_name='Тормозной прерыватель',
                                                         choices=BrakeInterrupter.choices, blank=True, null=True)

    class MotorCable(models.IntegerChoices):
        D1 = 1, 'Без дросселя: до 50м; С дросселем: до 100м'
        D2 = 2, 'Без дросселя: экран.кабель 35...100м в зависимости от номинала; неэкран. 50...150м. \n' \
                'С дросселем: экран.кабель 50...150м; неэкран. 90...225м'
        D3 = 3, 'Без дросселя: экран.кабель 50...150м в зависимости от номинала; неэкран. 75...225м. \n' \
                'С дросселем: экран.кабель 75...225м; неэкран. 115...325м'

    motor_cable_length = models.PositiveSmallIntegerField(verbose_name='Максимальная длина кабеля двигателя',
                                                          choices=MotorCable.choices, blank=True, null=True)

    quick_change_fans = models.BooleanField(verbose_name='Быстросъёмные вентиляторы', blank=True, null=True)
    removable_terminal_blocks = models.BooleanField(verbose_name='Съёмные клеммные колодки', blank=True, null=True)
    dual_circuit_cooling = models.BooleanField(verbose_name='Двухконтурное охлаждение', blank=True, null=True)

    class OperatingTemp(models.IntegerChoices):
        T1 = 1, '-10...+40'
        T2 = 2, '-10...+40(+50); \nСо снижением характеристик -10...+60'
        T3 = 3, '-20...+50; \nСо снижением характеристик -20...+60'

    operating_temp = models.PositiveSmallIntegerField(verbose_name='Рабочая температура, ℃',
                                                      choices=OperatingTemp.choices, blank=True, null=True)

    class Humidity(models.IntegerChoices):
        H90 = 1, 'Макс. 90%'
        H95 = 2, 'Макс. 95%'

    use_relative_humidity = models.PositiveSmallIntegerField(verbose_name='Относительная влажность при эксплуатации',
                                                             choices=Humidity.choices, blank=True, null=True)

    class Pressure(models.IntegerChoices):
        P86_106 = 1, '86...106'

    atmospheric_pressure_use = models.PositiveSmallIntegerField(
        verbose_name='Атмосферное давление при эксплуатации, кПа', choices=Pressure.choices, blank=True, null=True)

    class Altitude(models.IntegerChoices):
        A1 = 1, 'До 1000м'
        A2 = 2, 'До 1000м; Свыше 1000м со снижением характеристик'

    installation_altitude = models.PositiveSmallIntegerField(verbose_name='Высота установки',
                                                             choices=Altitude.choices, blank=True, null=True)

    class WallToWall(models.IntegerChoices):
        W1 = 1, 'Допускается для ПЧ от 45 кВт включительно; \nДо 45 кВт: зазор 10мм'
        W2 = 2, 'Допускается при макс.окруж.темп. до -40℃, \nдо -50℃ со снижением характеристик'

    wall_to_wall_installation = models.PositiveSmallIntegerField(verbose_name='Монтаж "Стенка к стенке"',
                                                                 choices=WallToWall.choices, blank=True, null=True)

    class ProtectionDegree(models.IntegerChoices):
        D1 = 1, 'IP20'
        D2 = 2, 'IP21'
        D3 = 3, 'IP55'

    protection_degree = models.PositiveSmallIntegerField(verbose_name='Степень защиты',
                                                         choices=ProtectionDegree.choices, blank=True, null=True)

    class BoardsProtection(models.IntegerChoices):
        P0 = 0, 'Нет'
        P1 = 1, 'Специальное покрытие печатных плат'

    circuit_boards_protection = models.PositiveSmallIntegerField(verbose_name='Защита печатных плат',
                                                                 choices=BoardsProtection.choices,
                                                                 blank=True, null=True)

    main_control_functions = models.TextField('Основные функции управления', blank=True, null=True)

    description = models.TextField('Описание', blank=True, null=True)

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
    power = models.FloatField('Мощность')
    current = models.FloatField('Ток')
    VOLT_CHOICES = (
        (400, 400),
        (230, 230),
    )
    voltage = models.FloatField('Напряжение', default=380, choices=VOLT_CHOICES)

    def __str__(self):
        if self:
            return str(f'{self.article}')

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
        return str(f'{self.article}')

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
        return str(f'{self.price}')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

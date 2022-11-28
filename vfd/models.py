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
        P10 = 10, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...3.7кВт'
        P11 = 11, '1x230В: 0.2...2.2кВт; 3x400В: 0.75...2.2кВт'
        P20 = 20, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...5.5кВт'
        P30 = 30, '1x230В: 0.2...2.2кВт; 3x400В: 0.4...7.5кВт'
        P40 = 40, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...15кВт'
        P50 = 50, '1x230В: 0.2...2.2кВт; 3x400В: 0.4...22кВт'
        P51 = 51, '1x230В: 0.4...2.2кВт; 3x400В: 0.4...22кВт'
        P60 = 60, '3x400В: 0.75...37кВт'
        P70 = 70, '3x400В: 0.75...90кВт'
        P80 = 80, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...110кВт'
        P90 = 90, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...220кВт'
        P91 = 91, '1x230В: 0.75...2.2кВт; 3x400В: 0.75...220кВт'
        P100 = 100, '3x400В: 0.75...500кВт'
        P101 = 101, '3x400В: 0.75...630кВт'
        P102 = 102, '1x230В: 0.4...2.2кВт; 3x400В: 0.75...630кВт'
        P103 = 103, '1x230В: 0.75...2.2кВт; 3x400В: 0.75...630кВт'
        P104 = 104, '1x230В: 0.2...3.7кВт; 3x400В: 0.75...400кВт'

    power_range = models.PositiveSmallIntegerField(verbose_name='Диапазон мощностей',
                                                   choices=Power.choices, blank=True, null=True)

    class ControlMethods(models.IntegerChoices):
        C10 = 10, 'V/F (скалярное управление)'
        C20 = 20, 'V/F (скалярное управление), \nSVC (бездатчиковое векторное управление)'
        C30 = 30, 'V/F (скалярное управление), \nSVC (бездатчиковое векторное управление), \n' \
                  'VC (векторное управление с замкнутым контуром)'

    control_methods = models.PositiveSmallIntegerField(verbose_name='Методы управления',
                                                       choices=ControlMethods.choices, blank=True, null=True)

    class Motors(models.IntegerChoices):
        F1 = 1, 'IM (асинхронные)'
        F2 = 2, 'IM (асинхронные), PM (синхронные с постоянными магнитами)'
        F3 = 3, 'IM (асинхронные), PM (синхронные с постоянными магнитами), SynRM (синхронные реактивные)'

    motors = models.PositiveSmallIntegerField(verbose_name='Двигатели', choices=Motors.choices, blank=True, null=True)

    class MaximumFrequency(models.IntegerChoices):
        F10 = 10, '320'
        F20 = 20, '599; 90 кВт и выше: 400'
        F21 = 21, '500'
        F22 = 22, '400'
        F30 = 30, '599'
        F31 = 31, '600'
        F40 = 40, '999'
        F50 = 50, '3000 (V/F); 300 (SVC)'
        F51 = 51, '3200 (V/F); 300 (SVC)'
        F52 = 52, '3200 (V/F); 500 (SVC)'
        F53 = 53, '5000'

    maximum_output_frequency = models.PositiveSmallIntegerField(verbose_name='Максимальная выходная частота, Гц',
                                                                choices=MaximumFrequency.choices, blank=True, null=True)

    class Overload(models.IntegerChoices):
        P10 = 10, 'Лёгкий режим: 120% 60с; \nНормальный режим: 120% 60с, 160% 3с'
        P20 = 20, '150% 60с; 180% 3с'
        P21 = 21, 'G type: 150% 60с, 180% 3с; \nP type: 120% 60с, 150% 3с'
        P22 = 22, '150% 60с; 180% 2с; 200% 0.5c'
        P23 = 23, 'G type: 150% 60с; 180% 3с'
        P24 = 24, '150% 60с каждые 10 мин; 180% 2с'
        P30 = 30, '110% длит.; 150% 60с; 180% 5с'
        P31 = 31, 'Нормальный режим: 120% 60с, 150% 3с; \nТяжелый режим: 150% 60с, 200% 3с'
        P32 = 32, 'G type: 110% длит.; 150% 60с, 200% 4с; \nP type: 105% длит.; 120% 60с, 150% 1с'
        P33 = 33, '150% 60с; 180% 10с; 200% 1c'
        P34 = 34, 'G type: 150% 60с; 180% 10с; 200% 1c; \nP type: 120% 60с'

    overload_capacity = models.PositiveSmallIntegerField('Перегрузочная способность',
                                                         choices=Overload.choices, blank=True, null=True)

    class StartingTorque(models.IntegerChoices):
        S10 = 10, '150% / 0.5 Гц'
        S11 = 11, 'G type: 150% / 0.5 Гц (SVC)'
        S12 = 12, 'G type: 150% / 0.5 Гц (SVC);\nP type: 100% / 0.5 Гц'
        S13 = 13, '150% / 3 Гц (V/F), \n150% / 1 Гц (FVC)'
        S14 = 14, '150% / 3 Гц (V/F, SVC для IM в тяжёлом режиме)\n100% / 2.5 Гц (V/F, SVC для PM в тяжёлом режиме)'
        S15 = 15, '100% / 0.5 Гц (V/F); 150% / 0.5 Гц (SVC)'
        S16 = 16, '150% / 3(1) Гц (V/F); 150% / 0.5 Гц (SVC)'
        S17 = 17, 'G type: 150% / 0.5 Гц; \nP type: 100% / 0.5 Гц'
        S18 = 18, 'Auto torque boost, manual torque boost 0.1%-30%; Vector torque boost 100-150; ' \
                  'Start frequency 0.4Hz-20Hz'
        S19 = 19, '150% / 0.5 Гц (SVC)'
        S20 = 20, 'G type: 150% / 0.5 Гц (SVC), 180% / 0 Гц (VC);\nP type: 100% / 0.5 Гц'
        S21 = 21, 'Auto torque boost, manual torque boost 0.1%-30%; ' \
                  'Cut-off frequency of torque boost 0Hz to maximum output frequency'
        S22 = 22, 'До 180% от номинального (Функция намагничивания постоянным током)'

    starting_torque = models.PositiveSmallIntegerField('Пусковой момент', choices=StartingTorque.choices,
                                                       blank=True, null=True)

    class CarrierFrequency(models.IntegerChoices):
        # - Например, при несущей частоте ШИМ более 8 кГц происходит существенное снижение шума от электродвигателя,
        # что позволяет применять их при автоматизации офисных и жилых зданий, медицинских и научных учреждений.
        # - Номинальные токи при данных температурах окружающей среды достигаются только при
        # частоте коммутации, установленной по умолчанию, либо меньшей.
        # Carrier frequency Low → high
        # Motor noise Big → small
        # Output current waveform Poor → good
        # Motor temperature rise High → low
        # Temperature rise of frequency inverter Low → high
        # Leakage current Small → big
        # External radiation interference Small → big
        S20 = 20, '2...12 (Default: 3)'
        S21 = 21, '2...15'
        S22 = 22, '2...15 (Default: 4)'
        S23 = 23, '2...16 (Default: 4/3)'
        S24 = 24, '1...16/10/5 (Default: 6/4.5/3/1.8)'
        S25 = 25, '0.5...16'
        S26 = 26, '4...16 (Default: 4)'
        S30 = 30, '2...15/10/9 (Default: 8/6/4)'
        S31 = 31, '1...14 (Default: 8)'
        S32 = 32, '1...15 (Default: 8/4/2)'

    carrier_frequency = models.PositiveSmallIntegerField('Несущая частота ШИМ, кГц', choices=CarrierFrequency.choices,
                                                         blank=True, null=True)

    class MultiPump(models.IntegerChoices):
        W0 = 0, 'Нет'
        W10 = 10, 'Да, 2 насоса'
        W20 = 20, 'Да, до 3 насосов'
        W30 = 30, 'Да, до 4 насосов'
        W40 = 40, 'Да, до 8 насосов'

    multi_pump_system = models.PositiveSmallIntegerField(verbose_name='Много-насосный режим',
                                                         choices=MultiPump.choices, blank=True, null=True)

    class DifferentEngines(models.IntegerChoices):
        D0 = 0, 'Нет'
        D20 = 20, '2 группы параметров двигателей'
        D40 = 40, 'До 4 независимых групп параметров двигателя'

    different_engines_work = models.PositiveSmallIntegerField(verbose_name='Работа с разными двигателями',
                                                              choices=DifferentEngines.choices, blank=True, null=True)

    fire_mode = models.BooleanField(verbose_name='Пожарный режим', blank=True, null=True)
    sleep_mode = models.BooleanField(verbose_name='Спящий режим', blank=True, null=True)
    flying_start = models.BooleanField(verbose_name='Подхват на ходу', blank=True, null=True)

    class SkipFrequency(models.IntegerChoices):
        F0 = 0, 'Нет'
        F1 = 10, 'Пропуск одной полосы частот'
        F2 = 20, 'Пропуск 2-х полос частот'
        F3 = 30, 'Пропуск 3-х полос частот'
        F4 = 40, 'Пропуск 4-х полос частот'

    skip_frequency = models.PositiveSmallIntegerField(verbose_name='Пропуск критических частот',
                                                      choices=SkipFrequency.choices, blank=True, null=True)

    # Встроенная функция энергосбережения существенно уменьшает потребление электроэнергии
    # при работе в режиме ПИД-регулирования.
    automatic_energy_saving = models.BooleanField(verbose_name='Автоматическое энергосбережение', blank=True, null=True)

    class CoolingFanControl(models.IntegerChoices):
        F0 = 0, 'Нет'
        F20 = 20, 'Режим автоматического управления / работает всё время при включении питания'
        F50 = 50, 'На выбор 5 режимов работы вентилятора'
        F51 = 51, 'На выбор 4 режима работы вентилятора'

    cooling_fan_control = models.PositiveSmallIntegerField(verbose_name='Управление вентилятором охлаждения',
                                                           choices=CoolingFanControl.choices, blank=True, null=True)

    class EngineProtection(models.IntegerChoices):
        P1 = 1, 'Перегрузка по току, перенапряжение, перегрев, потеря фазы и др.'

    engine_protection = models.PositiveSmallIntegerField('Защита двигателя', choices=EngineProtection.choices,
                                                         blank=True, null=True)

    class StopPrevention(models.IntegerChoices):
        P10 = 10, 'Токоограничение при разгоне, замедлении и работе (общая настройка)'
        P11 = 11, 'Токоограничение при работе (общая настройка)'
        P20 = 20, 'Токоограничение при разгоне, замедлении и работе (независимые настройки)'
        P21 = 21, 'Токоограничение при разгоне, работе (независимые настройки)'

    stop_prevention = models.PositiveSmallIntegerField('Предотвращение перегрузки',
                                                       choices=StopPrevention.choices, blank=True, null=True)

    automatic_start_after_power_loss = models.BooleanField('Преодоление провалов напряжения питания',
                                                           blank=True, null=True)

    class InputsOutputs(models.IntegerChoices):
        I10 = 10, 'DI: 4; AI: 1; TO: 0; RO: 1; AO: 1'
        I20 = 20, 'DI: 4; AI: 2; TO: 0; RO: 1; AO: 1'
        I30 = 30, 'DI: 5; AI: 1; TO: 1; RO: 1; AO: 1'
        I40 = 40, 'DI: 6; AI: 2; TO: 0; RO: 1; AO: 1'
        I41 = 41, 'DI: 5; AI: 2; TO: 1; RO: 1; AO: 1'
        I50 = 50, 'DI: 5; AI: 2; TO: 1; RO: 2; AO: 2'
        I60 = 60, 'DI: 6; AI: 2; TO: 1; RO: 2; AO: 2'
        I61 = 61, 'DI: 6; AI: 2; TO: 2; RO: 1; AO: 2'
        I70 = 70, 'DI: 7; AI: 2; TO: 3; RO: 1; AO: 1'
        I71 = 71, 'DI: 7; AI: 2; TO: 2; RO: 2; AO: 1'
        I72 = 72, 'DI: 8; AI: 2; TO: 2; RO: 1; AO: 1'
        I80 = 80, 'DI: 7; AI: 3; TO: 2; RO: 1; AO: 2'
        I81 = 81, 'DI: 8; AI: 2; TO: 2; RO: 2; AO: 2'
        I90 = 90, 'DI: 10; AI: 3; TO: 0; RO: 3; AO: 2'

    inputs_outputs = models.PositiveSmallIntegerField(verbose_name='Входы/выходы',
                                                      choices=InputsOutputs.choices, blank=True, null=True)

    io_expansion_boards = models.BooleanField(verbose_name='Платы расширения входов-выходов', blank=True, null=True)

    class PulseFrequencySetting(models.IntegerChoices):
        IO0 = 0, 'Нет'
        IO1 = 1, 'Плата расширения'
        IO2 = 2, 'Да'

    pulse_frequency_setting = models.PositiveSmallIntegerField('Импульсное задание частоты',
                                                               choices=PulseFrequencySetting.choices,
                                                               blank=True, null=True)

    class ControlPanel(models.IntegerChoices):
        P10 = 10, 'LED 4x7'
        P20 = 20, 'LED 5x7'
        P30 = 30, 'LED двухстрочный'
        P31 = 31, 'LED 5x7 (LCD опционально)'
        P32 = 32, 'LED двухстрочный (LCD опционально)'
        P60 = 60, 'LCD дисплей'
        P61 = 61, 'LCD базовая (LCD интеллектуальная опционально)'

    control_panel = models.PositiveSmallIntegerField('Панель управления', choices=ControlPanel.choices,
                                                     blank=True, null=True)

    class Potentiometer(models.IntegerChoices):
        P0 = 0, 'Нет'
        P10 = 10, 'Дополнительная плата потенциометра'
        P20 = 20, 'Потенциометр в панели управления'
        P30 = 30, 'Нажимное колёсико-энкодер'

    potentiometer = models.PositiveSmallIntegerField('Потенциометр', choices=Potentiometer.choices,
                                                     blank=True, null=True)

    control_panel_included = models.BooleanField('Панель управления в комплекте', blank=True, null=True)

    class RemovablePanel(models.IntegerChoices):
        P0 = 0, 'Нет'
        P10 = 10, 'Для моделей от 22 кВт'
        P20 = 20, 'Да'

    removable_control_panel = models.PositiveSmallIntegerField('Съёмная панель', choices=RemovablePanel.choices,
                                                               blank=True, null=True)

    class PanelAtDistance(models.IntegerChoices):
        P0 = 0, 'Нет'
        P10 = 10, 'Да, при помощи кабеля-аксессуара'
        P11 = 11, 'Да'
        P20 = 20, 'Да, соединение обычным патч-кордом'

    control_panel_at_distance = models.PositiveSmallIntegerField('Выносная панель', choices=PanelAtDistance.choices,
                                                                 blank=True, null=True)

    class Configurations(models.IntegerChoices):
        C0 = 0, 'Нет'
        C10 = 10, 'Группировка параметров по применениям'
        C11 = 11, 'Макросы по применениям'
        C20 = 20, 'Макросы, мастера настроек'

    pre_configurations = models.PositiveSmallIntegerField(verbose_name='Предварительные конфигурации (Макросы)',
                                                          choices=Configurations.choices, blank=True, null=True)

    class BackupSettings(models.IntegerChoices):
        S0 = 0, 'Нет'
        S20 = 20, 'Да (LCD панель)'
        S21 = 21, 'Да (только для дистанционного управления)'
        S40 = 40, 'Да'

    copy_backup_settings = models.PositiveSmallIntegerField(verbose_name='Копирование/бэкап настроек',
                                                            choices=BackupSettings.choices, blank=True, null=True)
    pid_controller = models.IntegerField(verbose_name='Встроенный ПИД-регулятор', blank=True, null=True)

    class Communications(models.IntegerChoices):
        C0 = 0, 'Нет'
        C10 = 10, 'Плата расширения: Modbus RTU'
        C20 = 20, 'Платы расширения: Modbus RTU, Profibus DP'
        C30 = 30, 'Встроен: Modbus RTU'
        C40 = 40, 'Встроен: Modbus RTU; Платы расширения: Profibus DP'
        C41 = 41, 'Платы расширения: Modbus RTU, Ethernet, Profibus DP, ProfiNet IO, DeviceNet, CANopen, EtherCAT'
        C50 = 50, 'Встроен: Modbus RTU; Платы расширения: Ethernet, Profibus DP'
        C60 = 60, 'Встроен: Modbus RTU; Платы расширения: Profibus DP, CANopen, CANlink'
        C70 = 70, 'Встроен: Modbus RTU; Платы расширения: Ethernet, DeviceNet, CANopen, Profibus DP'
        C80 = 80, 'Встроены: Modbus RTU, BACnet; Платы расширения: Ethernet, DeviceNet, CANopen, Profibus DP'

    communications = models.PositiveSmallIntegerField('Протоколы связи',
                                                      choices=Communications.choices, blank=True, null=True)

    class Plc(models.IntegerChoices):
        PO = 0, 'Нет'
        P2 = 2, 'ПЛК на 2000 шагов'
        P3 = 3, 'ПЛК на 10000 шагов'

    built_in_plc = models.PositiveSmallIntegerField(verbose_name='Встроенный ПЛК',
                                                    choices=Plc.choices, blank=True, null=True)

    class Encoder(models.IntegerChoices):
        PO = 0, 'Нет'
        P10 = 10, 'Импульсный вход (плата расширения)'
        P20 = 20, 'Импульсный вход'
        P50 = 50, 'Плата расширения энкодера (ABZ, UVW, Rotary transformer)'
        P51 = 51, 'Плата расширения энкодера'

    encoder_support = models.PositiveSmallIntegerField(verbose_name='Подключение энкодера',
                                                       choices=Encoder.choices, blank=True, null=True)
    sto_function = models.BooleanField(verbose_name='Стандарт безопасности STO', blank=True, null=True)

    class ExternalPower(models.IntegerChoices):
        P0 = 0, 'Нет'
        P1 = 1, 'Опциональная плата'
        P2 = 2, 'Да'

    external_power_24v = models.PositiveSmallIntegerField(verbose_name='Подключение резервного питания +24В',
                                                          choices=ExternalPower.choices, blank=True, null=True)

    class Usb(models.IntegerChoices):
        U0 = 0, 'Нет'
        U1 = 1, 'Есть (загрузка и выгрузка даже без включения питания)'

    built_in_usb = models.PositiveSmallIntegerField(verbose_name='Встроенный порт USB',
                                                    choices=Usb.choices, blank=True, null=True)

    class PCSoft(models.IntegerChoices):
        S0 = 0, 'Нет'
        S30 = 30, 'Да'

    pc_soft = models.PositiveSmallIntegerField(verbose_name='Софт для отладки на ПК',
                                               choices=PCSoft.choices, blank=True, null=True)

    class EmcFilter(models.IntegerChoices):
        E0 = 0, 'Нет'
        E10 = 10, '1x230В: C3; 3x400В: контур ЭМС-фильтра'
        E11 = 11, 'Контур ЭМС-фильтра'
        E20 = 20, 'C3 (для эксплуатации в промышленной зоне)'
        E30 = 30, 'C2 (для эксплуатации в жилой зоне)'

    emc_filter = models.PositiveSmallIntegerField(verbose_name='Встроенный EMC фильтр',
                                                  choices=EmcFilter.choices, blank=True, null=True)

    class ChokeDc(models.IntegerChoices):
        C0 = 0, 'Нет'
        C10 = 10, 'Опция от 75кВт'
        C20 = 20, 'Опция 45...400кВт, встроен от 450кВт'
        C30 = 30, 'Опция'
        C40 = 40, 'Встроен на мощности 11, 15 кВт и от 200 кВт'
        C50 = 50, 'Встроен на мощности от 45 кВт'
        C60 = 60, 'Встроен на мощности от 37 кВт'
        C70 = 70, 'Встроен'

    choke_dc_link = models.PositiveSmallIntegerField(verbose_name='Дроссель в звене постоянного тока',
                                                     choices=ChokeDc.choices, blank=True, null=True)

    class BrakeInterrupter(models.IntegerChoices):
        C0 = 0, 'Нет'
        C10 = 10, 'Встроен на мощности до 15 кВт'
        C20 = 20, 'Встроен на мощности до 22 кВт'
        C30 = 30, 'Встроен на мощности до 30 кВт'
        C40 = 40, 'Встроен на мощности до 37 кВт'
        C50 = 50, 'Встроен на мощности до 45 кВт'
        C60 = 60, 'Встроен'

    brake_interrupter = models.PositiveSmallIntegerField(verbose_name='Тормозной прерыватель',
                                                         choices=BrakeInterrupter.choices, blank=True, null=True)

    class MotorCable(models.IntegerChoices):
        D10 = 10, 'Без дросселя: до 50м; С дросселем: до 100м'
        D11 = 11, 'Если длина кабелей двигателя превышает 50 м, рекомендуется использовать моторный дроссель.'
        D12 = 12, 'Без дросселя: до 50м; С дросселем: до 100м; EMC C3: до 30м'
        D20 = 20, 'Если длина кабелей двигателя превышает 100 м, рекомендуется использовать моторный дроссель.'
        D30 = 30, 'Без дросселя: экран.кабель 35...100м в зависимости от номинала; неэкран. 50...150м. \n' \
                  'С дросселем: экран.кабель 50...150м; неэкран. 90...225м'
        D40 = 40, 'Без дросселя: экран.кабель 50...150м в зависимости от номинала; неэкран. 75...225м. \n' \
                  'С дросселем: экран.кабель 75...225м; неэкран. 115...325м'

    motor_cable_length = models.PositiveSmallIntegerField(verbose_name='Максимальная длина кабеля двигателя',
                                                          choices=MotorCable.choices, blank=True, null=True)

    quick_change_fans = models.BooleanField(verbose_name='Быстросъёмные вентиляторы', blank=True, null=True)
    dual_circuit_cooling = models.BooleanField(verbose_name='Двухконтурное охлаждение', blank=True, null=True)

    class OperatingTemp(models.IntegerChoices):
        T10 = 10, '-10...+40'
        T20 = 20, '-10...+40; \nСо снижением характеристик -10...+50'
        T21 = 21, '-10...+40(50)'
        T30 = 30, '-10...+40(50); \nСо снижением характеристик -10...+60'
        T40 = 40, '-10...+50; \nСо снижением характеристик -10...+60'
        T50 = 50, '-20...+50; \nСо снижением характеристик -20...+60'

    operating_temp = models.PositiveSmallIntegerField(verbose_name='Рабочая температура, ℃',
                                                      choices=OperatingTemp.choices, blank=True, null=True)

    class Humidity(models.IntegerChoices):
        H20 = 20, 'Макс. 60%'
        H40 = 40, 'Макс. 90%'
        H50 = 50, 'Макс. 95%'

    use_relative_humidity = models.PositiveSmallIntegerField(verbose_name='Относительная влажность при эксплуатации',
                                                             choices=Humidity.choices, blank=True, null=True)

    class Altitude(models.IntegerChoices):
        A1 = 1, 'До 1000м'
        A2 = 2, 'До 1000м; Свыше 1000м со снижением характеристик'

    installation_altitude = models.PositiveSmallIntegerField(verbose_name='Высота установки',
                                                             choices=Altitude.choices, blank=True, null=True)

    class WallToWall(models.IntegerChoices):
        W0 = 0, 'Нет'
        W10 = 10, 'Допускается для ПЧ от 45 кВт включительно; \nДо 45 кВт: зазор 10мм'
        W20 = 20, 'Допускается при -20...+40℃, \nдо +50℃ со снижением характеристик'
        W21 = 21, 'Допускается при -20...+40℃'
        W30 = 30, 'Допускается'

    wall_to_wall_installation = models.PositiveSmallIntegerField(verbose_name='Монтаж "Стенка к стенке"',
                                                                 choices=WallToWall.choices, blank=True, null=True)

    class RailwayMounting(models.IntegerChoices):
        R0 = 0, 'Нет'
        R10 = 10, 'Монтажный комплект на DIN-рейку'
        R20 = 20, 'Да'

    railway_mounting = models.PositiveSmallIntegerField(verbose_name='Монтаж на дин-рейку',
                                                        choices=RailwayMounting.choices, blank=True, null=True)

    class ProtectionDegree(models.IntegerChoices):
        D1 = 1, 'IP20'
        D2 = 2, 'IP21'
        D3 = 3, 'IP55'

    protection_degree = models.PositiveSmallIntegerField(verbose_name='Степень защиты',
                                                         choices=ProtectionDegree.choices, blank=True, null=True)

    class BoardsProtection(models.IntegerChoices):
        P0 = 0, 'Нет'
        P10 = 10, 'Специальное покрытие печатных плат'
        P11 = 11, 'Трёхслойное защитное покрытие'

    circuit_boards_protection = models.PositiveSmallIntegerField(verbose_name='Защита печатных плат',
                                                                 choices=BoardsProtection.choices,
                                                                 blank=True, null=True)

    class MinimumSize(models.IntegerChoices):
        # По габаритам HV10 (по глубине) меньше чем ACS355, что позволяет засунуть этот ПЧ в корпус глубиной 150мм
        # (если речь идет о стандартных типоразмерах большинства корпусов производства РБ и РФ типа ЩМП:
        # 1 - 395х410х220 мм; 2 - 500х400х220 мм; и т.д.). НО! Применяя корпус глубиной 150 мм, мы можем сэкономить
        # место, например, в венткамере, где шкаф управления с ПЧ закреплен прямо на вентустановке.
        # Массовое применение 1ф ПЧ - управление различными задвижками, т.е. открыть/закрыть. В этом случае мелкий
        # корпус позволяет без проблем разместить ПЧ в непосредственной близости от исполнительного механизма.

        # "HV100 серия, по высоте (глубине) на 5мм меньше чем 355. В связи с этим, эту серию уже придется монтировать
        # в корпуса глубиной 220мм. По ширине эта серия на 25 мм больше, а учесть что 355 шириной всего 70 мм,
        # то HV100 ""съедает"" примерно 35% места на монтажной панели при компоновке в ряд.
        P30 = 30, '212x95x154'  # HV100
        P40 = 40, '202x70x161'  # ACS355
        P42 = 42, '142x72x159'  # MS300
        P50 = 50, '170x78x134'  # HV10
        P51 = 51, '142x72x143'  # ME300

        P41 = 41, '176x90x145'  # HV480
        P31 = 31, '186x125x170'  # HV610

    minimum_size = models.PositiveSmallIntegerField(verbose_name='Минимальный габарит, ВхШхГ',
                                                    choices=MinimumSize.choices, blank=True, null=True)

    class PackageSet(models.IntegerChoices):
        P0 = 0, 'Нет'
        P10 = 10, 'Плотный картон, вспененный полиэтилен, сокращённый мануал'
        P11 = 11, 'Плотный картон, вспененный полиэтилен, полный мануал'
        P12 = 12, 'Плотный картон, краткая инструкция по вводу в эксплуатацию'
        P30 = 30, 'Плотный картон, надувная пузырчатая пленка, сокращённый мануал'
        P31 = 31, 'Плотный картон, надувная пузырчатая пленка, полный мануал'
        P32 = 32, 'Плотный картон, сокращённый мануал'

    package_set = models.PositiveSmallIntegerField(verbose_name='Комплект поставки, упаковка',
                                                   choices=PackageSet.choices, blank=True, null=True)

    class CaseQuality(models.IntegerChoices):
        P10 = 10, 'Прочный корпус; неудобное снятие клеммной крышки, дребезжит крышка вентилятора'
        P30 = 30, 'Прочный корпус, качественная сборка; чёрный матовый, не вонючий пластик'
        P31 = 31, 'Прочный корпус, качественная сборка'

    case_quality = models.PositiveSmallIntegerField(verbose_name='Качество корпуса',
                                                    choices=CaseQuality.choices, blank=True, null=True)

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
    series = models.ForeignKey(Series, verbose_name='Серия', on_delete=models.PROTECT)
    power = models.FloatField('Мощность')
    current = models.FloatField('Ток', blank=True, null=True)
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

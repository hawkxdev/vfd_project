from django.contrib import admin
from django.utils.safestring import mark_safe

from vfd.models import *

admin.site.register(Country)
admin.site.register(EquipmentLine)
admin.site.register(Application)
admin.site.register(Category)
admin.site.register(AccessoryType)
admin.site.register(Accessory)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """Серии ПЧ"""
    list_display = ('brand', 'name')
    list_filter = ('brand', 'name')
    readonly_fields = ('get_image', 'id')
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': (('brand', 'name', 'category'),)
        }),
        (None, {
            'fields': (('get_image', 'image', 'applications'),)
        }),
        (None, {
            'fields': (('power_range',),)
        }),
        ('Характеристики управления', {
            'fields': (('control_methods', 'motors', 'maximum_output_frequency', 'overload_capacity', 'starting_torque',
                        'main_control_functions', 'multi_pump_system', 'engine_cascade_control',
                        'different_engines_work', 'fire_mode', 'sleep_mode', 'flying_start', 'skip_frequency',
                        'automatic_energy_saving'),)
        }),
        ('Характеристики защиты', {
            'fields': (('engine_protection', 'stop_prevention', 'automatic_start_after_power_loss'),)
        }),
        ('Плата управления', {
            'fields': (('inputs_outputs', 'io_expansion_boards', 'pulse_frequency_setting'),)
        }),
        ('Опции', {
            'fields': (('control_panel', 'control_panel_desc', 'control_panel_included', 'control_panel_at_distance',
                        'pre_configurations', 'copy_backup_settings', 'pid_controller', 'built_in_communication',
                        'additional_communications', 'built_in_plc', 'encoder_support', 'sto_function',
                        'external_power_24v', 'built_in_usb'),)
        }),
        ('Дополнительное оборудование', {
            'fields': (('emc_filter', 'choke_dc_link', 'brake_interrupter', 'motor_cable_length', 'quick_change_fans',
                        'removable_terminal_blocks', 'dual_circuit_cooling'),)
        }),
        ('Условия эксплуатации, хранения и транспортировки', {
            'fields': (('operating_temp', 'use_relative_humidity', 'atmospheric_pressure_use', 'installation_altitude',
                        'wall_to_wall_installation', 'protection_degree', 'circuit_boards_protection'),)
        }),
        ('Описание', {
            'fields': (('description', 'id'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70">')

    get_image.short_description = 'Картинка'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['control_panel_desc'].widget.attrs['style'] = 'width: 45em; height: 4em;'
        return form


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Бренды ПЧ"""
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="70">')

    get_image.short_description = 'Картинка'


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    """Цены на ПЧ"""
    list_display = ('get_brand', 'frequency_drive', 'accessory', 'get_power', 'price', 'get_currency', 'supplier')
    list_filter = ('supplier', 'frequency_drive__series__brand', 'frequency_drive__series')
    list_display_links = ('frequency_drive', 'accessory', 'get_power')

    def get_brand(self, obj):
        if obj.frequency_drive:
            return f'{obj.frequency_drive.series.brand}'
        elif obj.accessory:
            return f'{obj.accessory.series.first().brand}'

    def get_power(self, obj):
        if obj.frequency_drive:
            return f'{obj.frequency_drive.power}'

    def get_currency(self, obj):
        if obj.frequency_drive or obj.accessory:
            return f'{obj.supplier.currency}'

    get_brand.short_description = 'Бренд'
    get_power.short_description = 'Мощность'
    get_currency.short_description = 'Валюта'


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Поставщики"""
    readonly_fields = ('id',)


@admin.register(FrequencyDrive)
class FrequencyDriveAdmin(admin.ModelAdmin):
    """ПЧ"""
    list_display = ('article', 'power', 'current', 'voltage', 'series')
    list_filter = ('series__brand', 'series')

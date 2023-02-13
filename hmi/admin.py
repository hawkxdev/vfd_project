from django.contrib import admin
from django.utils.safestring import mark_safe

from hmi.models import *


@admin.register(HmiSeries)
class SeriesAdmin(admin.ModelAdmin):
    """Серия HMI"""
    list_display = ('brand', 'name', 'id')
    list_display_links = ('name',)
    list_filter = ('brand', 'name')
    # readonly_fields = ('get_image', 'id')
    # save_on_top = True
    # save_as = True
    #
    # fieldsets = (
    #     (None, {
    #         'fields': (('brand', 'name', 'category'),)
    #     }),
    #     (None, {
    #         'fields': (('get_image', 'image', 'applications'),)
    #     }),
    #     (None, {
    #         'fields': (('power_range',),)
    #     }),
    #     ('Характеристики управления', {
    #         'fields': (('control_methods', 'motors', 'maximum_output_frequency', 'overload_capacity', 'starting_torque',
    #                     'carrier_frequency', 'multi_pump_system',
    #                     'different_engines_work', 'fire_mode', 'sleep_mode', 'flying_start', 'skip_frequency',
    #                     'automatic_energy_saving', 'cooling_fan_control'),)
    #     }),
    #     ('Характеристики защиты', {
    #         'fields': (('engine_protection', 'stop_prevention', 'automatic_start_after_power_loss'),)
    #     }),
    #     ('Плата управления', {
    #         'fields': (('inputs_outputs', 'io_expansion_boards', 'pulse_frequency_setting'),)
    #     }),
    #     ('Опции', {
    #         'fields': (('control_panel', 'potentiometer', 'removable_control_panel', 'control_panel_included',
    #                     'control_panel_at_distance', 'pre_configurations', 'copy_backup_settings', 'pid_controller',
    #                     'communications', 'built_in_plc', 'encoder_support', 'sto_function', 'external_power_24v',
    #                     'built_in_usb', 'pc_soft'),)
    #     }),
    #     ('Дополнительное оборудование', {
    #         'fields': (('emc_filter', 'choke_dc_link', 'brake_interrupter', 'motor_cable_length', 'quick_change_fans',
    #                     'dual_circuit_cooling'),)
    #     }),
    #     ('Условия эксплуатации, хранения и транспортировки', {
    #         'fields': (('operating_temp', 'use_relative_humidity', 'installation_altitude', 'wall_to_wall_installation',
    #                     'railway_mounting', 'protection_degree', 'circuit_boards_protection', 'minimum_size',
    #                     'package_set', 'case_quality'),)
    #     }),
    #     ('Описание', {
    #         'fields': (('description', 'id'),)
    #     }),
    # )
    #
    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.image.url} width="70">')
    #
    # get_image.short_description = 'Картинка'

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['control_panel_desc'].widget.attrs['style'] = 'width: 45em; height: 4em;'
    #     return form


@admin.register(HmiModel)
class ModelAdmin(admin.ModelAdmin):
    """Модель HMI"""
    list_display = ('series', 'article', 'id')
    list_display_links = ('article',)
    list_filter = ('series__brand', 'series__name')

    readonly_fields = ('get_image_1', 'get_image_2', 'id')
    save_on_top = True
    save_as = True

    fieldsets = (
        (None, {
            'fields': (
                ('series', 'id'),
                ('article',),
                ('name',),
                ('get_image_1', 'image1'),
                ('get_image_2', 'image2'),
            )
        }),
        ('Характеристики', {
            'fields': (
                ('diagonal', 'resolution', 'display_type', 'supply_voltage', 'protection_degree'),
                ('cpu', 'flash_rom', 'ram'),
                ('communication_interfaces', 'com_port', 'ethernet_port', 'usb_port'),
                ('sd_card', 'speaker', 'audio_output', 'real_time_clock', 'input_in_russian'),
            )
        }),
        ('Технологии', {
            'fields': (
                ('network_technologies', 'cloud_technology', 'opc_ua_support', 'printer_communication'),
            )
        }),
        ('Мультимедиа', {
            'fields': (
                ('video_playback_from_media', 'vga_playback', 'ip_cameras_support', 'analog_cameras_support'),
            )
        }),
        ('Софт', {
            'fields': (
                ('pc_software', 'russian_software', 'communication_drivers', 'library_visualization_elements',
                 'gif_animation'),
                ('data_archiving', 'recipe', 'macro', 'script', 'user_rights_separation'),
                ('trends', 'pdf_support', 'simulation'),
            )
        }),
        ('Условия эксплуатации, хранения и транспортировки', {
            'fields': (
                ('operating_temp', 'storage_temp', 'vibration_resistance', 'humidity', 'dimensions', 'weight'),
            )
        }),
    )

    def get_image_1(self, obj):
        return mark_safe(f'<img src={obj.image1.url} width="70">')

    get_image_1.short_description = 'Картинка1'

    def get_image_2(self, obj):
        return mark_safe(f'<img src={obj.image2.url} width="70">')

    get_image_2.short_description = 'Картинка2'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['name'].widget.attrs['style'] = 'width: 80em;'
        return form

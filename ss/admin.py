from django.contrib import admin
from django.utils.safestring import mark_safe

from ss.models import *

# admin.site.register(EquipmentLine)
#
# @admin.register(Series)
# class SeriesAdmin(admin.ModelAdmin):
#     """Серии ПЧ"""
#     list_display = ('brand', 'name', 'id')
#     list_filter = ('brand', 'name')
#     list_display_links = ('brand', 'name')
#     readonly_fields = ('get_image', 'id')
#     save_on_top = True
#     save_as = True
#
#     fieldsets = (
#         (None, {
#             'fields': (('brand', 'name', 'category'),)
#         }),
#         (None, {
#             'fields': (('get_image', 'image', 'applications'),)
#         }),
#         (None, {
#             'fields': (('power_range',),)
#         }),
#         ('Характеристики управления', {
#             'fields': (('control_methods', 'motors', 'maximum_output_frequency', 'overload_capacity', 'starting_torque',
#                         'carrier_frequency', 'multi_pump_system',
#                         'different_engines_work', 'fire_mode', 'sleep_mode', 'flying_start', 'skip_frequency',
#                         'automatic_energy_saving', 'cooling_fan_control'),)
#         }),
#         ('Характеристики защиты', {
#             'fields': (('engine_protection', 'stop_prevention', 'automatic_start_after_power_loss'),)
#         }),
#         ('Плата управления', {
#             'fields': (('inputs_outputs', 'io_expansion_boards', 'pulse_frequency_setting'),)
#         }),
#         ('Опции', {
#             'fields': (('control_panel', 'potentiometer', 'removable_control_panel', 'control_panel_included',
#                         'control_panel_at_distance', 'pre_configurations', 'copy_backup_settings', 'pid_controller',
#                         'communications', 'built_in_plc', 'encoder_support', 'sto_function', 'external_power_24v',
#                         'built_in_usb', 'pc_soft'),)
#         }),
#         ('Дополнительное оборудование', {
#             'fields': (('emc_filter', 'choke_dc_link', 'brake_interrupter', 'motor_cable_length', 'quick_change_fans',
#                         'dual_circuit_cooling'),)
#         }),
#         ('Условия эксплуатации, хранения и транспортировки', {
#             'fields': (('operating_temp', 'use_relative_humidity', 'installation_altitude', 'wall_to_wall_installation',
#                         'railway_mounting', 'protection_degree', 'circuit_boards_protection'),)
#         }),
#         ('Описание', {
#             'fields': (('description', 'id'),)
#         }),
#     )
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.image.url} width="70">')
#
#     get_image.short_description = 'Картинка'
#
#     # def get_form(self, request, obj=None, **kwargs):
#     #     form = super().get_form(request, obj, **kwargs)
#     #     form.base_fields['control_panel_desc'].widget.attrs['style'] = 'width: 45em; height: 4em;'
#     #     return form

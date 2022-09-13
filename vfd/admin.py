from django.contrib import admin
from django.utils.safestring import mark_safe

from vfd.models import *

admin.site.register(Country)
admin.site.register(EquipmentLine)
admin.site.register(Brand)
admin.site.register(Application)
admin.site.register(Category)
admin.site.register(FrequencyDrive)
admin.site.register(Supplier)
admin.site.register(Price)
admin.site.register(AccessoryType)
admin.site.register(Accessory)


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    """Серии ПЧ"""
    list_display = ('brand', 'name')
    list_filter = ('brand', 'name')
    readonly_fields = ('get_image',)
    save_on_top = True

    fieldsets = (
        (None, {
            'fields': (('brand', 'name', 'category'),)
        }),
        (None, {
            'fields': (('get_image', 'image',),)
        }),
        (None, {
            'fields': (('power_min', 'power_max', 'applications'),)
        }),
        ('Характеристики управления', {
            'fields': (('control_methods', 'starting_torque', 'setting_vf_characteristic', 'speed_control_range',
                        'torque_limitation', 'torque_accuracy', 'maximum_output_frequency',
                        'output_frequency_accuracy', 'frequency_set_discreteness', 'overload_capacity',
                        'frequency_set_signals', 'acceleration_deceleration_time', 'main_control_functions',
                        'engine_cascade_control', 'multi_pump_system', 'fire_mode', 'sleep_mode', 'flying_start',
                        'skip_frequency', 'automatic_energy_saving',
                        'control_built_in_fan', 'engine_protection', 'overcurrent_protection',
                        'overvoltage_protection', 'temperature_protection', 'stop_prevention',
                        'automatic_start_after_power_loss', 'current_leakage_protection'),)
        }),
        ('Плата управления', {
            'fields': (('digital_inputs', 'analog_inputs', 'transistor_outputs', 'relay_outputs', 'analog_outputs'),)
        }),
        ('Опции', {
            'fields': (('control_panel', 'control_panel_included', 'control_panel_at_distance', 'pre_configurations',
                        'copy_backup_settings', 'pid_controller', 'built_in_communication', 'additional_communications',
                        'io_expansion_boards', 'built_in_plc', 'realtime_clock', 'encoder_support', 'sto_function'),)
        }),
        ('Дополнительное оборудование', {
            'fields': (('emc_filter', 'choke_dc_link', 'brake_interrupter', 'motor_cable_length', 'quick_change_fans',
                        'removable_terminal_blocks', 'dual_circuit_cooling'),)
        }),
        ('Условия эксплуатации, хранения и транспортировки', {
            'fields': (('installation_place', 'operating_temp', 'storage_temp', 'transport_temp',
                        'use_relative_humidity', 'storage_transportation_relative_humidity',
                        'atmospheric_pressure_use_storage', 'atmospheric_pressure_transportation',
                        'pollution_level_use', 'pollution_level_storage', 'pollution_level_transportation',
                        'installation_altitude', 'vibration', 'impact_resistance', 'mounting_position',
                        'wall_to_wall_installation', 'protection_degree', 'circuit_boards_protection'),)
        }),
        ('Описание', {
            'fields': (('description',),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70">')

    get_image.short_description = 'Картинка'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['control_methods'].widget.attrs['style'] = 'width: 80em;'
        form.base_fields['choke_dc_link'].widget.attrs['style'] = 'width: 40em;'
        form.base_fields['setting_vf_characteristic'].widget.attrs['style'] = 'width: 30em;'
        form.base_fields['torque_limitation'].widget.attrs['style'] = 'width: 55em;'
        form.base_fields['output_frequency_accuracy'].widget.attrs['style'] = 'width: 40em;'
        form.base_fields['frequency_set_discreteness'].widget.attrs['style'] = 'width: 45em;'
        form.base_fields['overload_capacity'].widget.attrs['style'] = 'width: 45em; height: 4em;'
        form.base_fields['frequency_set_signals'].widget.attrs['style'] = 'width: 25em;'
        form.base_fields['control_built_in_fan'].widget.attrs['style'] = 'width: 45em;'
        form.base_fields['overcurrent_protection'].widget.attrs['style'] = 'width: 40em; height: 4em;'
        form.base_fields['overvoltage_protection'].widget.attrs['style'] = 'width: 35em;'
        form.base_fields['stop_prevention'].widget.attrs['style'] = 'width: 35em;'
        form.base_fields['current_leakage_protection'].widget.attrs['style'] = 'width: 30em;'
        form.base_fields['installation_place'].widget.attrs['style'] = 'width: 35em;'
        form.base_fields['use_relative_humidity'].widget.attrs['style'] = 'width: 5em;'
        form.base_fields['storage_transportation_relative_humidity'].widget.attrs['style'] = 'width: 5em;'
        form.base_fields['atmospheric_pressure_use_storage'].widget.attrs['style'] = 'width: 5em;'
        form.base_fields['atmospheric_pressure_transportation'].widget.attrs['style'] = 'width: 5em;'
        form.base_fields['installation_altitude'].widget.attrs['style'] = 'width: 40em; height: 5em;'
        form.base_fields['vibration'].widget.attrs['style'] = 'width: 40em; height: 5em;'
        form.base_fields['impact_resistance'].widget.attrs['style'] = 'width: 40em; height: 6em;'
        form.base_fields['motor_cable_length'].widget.attrs['style'] = 'width: 45em; height: 7em;'
        form.base_fields['mounting_position'].widget.attrs['style'] = 'width: 40em;'
        form.base_fields['operating_temp'].widget.attrs['style'] = 'width: 40em; height: 4em;'
        form.base_fields['storage_temp'].widget.attrs['style'] = 'width: 5em;'
        form.base_fields['transport_temp'].widget.attrs['style'] = 'width: 5em;'
        form.base_fields['pollution_level_use'].widget.attrs['style'] = 'width: 10em;'
        form.base_fields['pollution_level_storage'].widget.attrs['style'] = 'width: 10em;'
        form.base_fields['pollution_level_transportation'].widget.attrs['style'] = 'width: 10em;'
        form.base_fields['wall_to_wall_installation'].widget.attrs['style'] = 'width: 40em;'
        form.base_fields['pre_configurations'].widget.attrs['style'] = 'width: 40em;'
        form.base_fields['control_panel'].widget.attrs['style'] = 'width: 45em; height: 4em;'
        form.base_fields['engine_cascade_control'].widget.attrs['style'] = 'width: 55em;'
        form.base_fields['circuit_boards_protection'].widget.attrs['style'] = 'width: 45em;'
        form.base_fields['additional_communications'].widget.attrs['style'] = 'width: 35em;'
        return form

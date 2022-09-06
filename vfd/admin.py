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
                        'frequency_set_signals', 'acceleration_deceleration_time'),)
        }),
        (None, {
            'fields': (('digital_inputs', 'analog_inputs', 'transistor_outputs', 'relay_outputs', 'analog_outputs'),)
        }),
        (None, {
            'fields': (('control_panel', 'control_panel_included',
                        'built_in_communication', 'additional_communications'),)
        }),
        (None, {
            'fields': (('emc_filter', 'choke_dc_link', 'brake_interrupter', 'built_in_plc'),)
        }),
        (None, {
            'fields': (('protection_degree', 'operating_temp'),)
        }),
        (None, {
            'fields': (('description',),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="90">')

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
        return form

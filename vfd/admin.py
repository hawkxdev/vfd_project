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

    fieldsets = (
        (None, {
            'fields': (('brand', 'name', 'category'),)
        }),
        (None, {
            'fields': (('power_min', 'power_max', 'applications', 'overload_capacity'),)
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
            'fields': (('get_image', 'image', 'description'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = "Изображение"

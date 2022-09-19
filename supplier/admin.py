from django.contrib import admin
from django.utils.safestring import mark_safe
from supplier.models import *

admin.site.register(Country)
# admin.site.register(EquipmentLine)


# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     """Бренды"""
#     readonly_fields = ('get_image',)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.logo.url} width="70">')
#
#     get_image.short_description = 'Картинка'
#
#
# @admin.register(Supplier)
# class SupplierAdmin(admin.ModelAdmin):
#     """Поставщики"""
#     readonly_fields = ('id',)

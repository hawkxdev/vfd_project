from django.db.models import Q

from vfd.models import FrequencyDrive, Accessory, Series, Supplier, Price


def get_vfd(article):
    try:
        vfd = FrequencyDrive.objects.get(article=article)
    except FrequencyDrive.DoesNotExist:
        vfd = None
    return vfd


def get_vfd_by_params(series, power, voltage):
    try:
        vfd = FrequencyDrive.objects.filter(series=series, power=power, voltage=voltage).first()
    except FrequencyDrive.DoesNotExist:
        vfd = None
    return vfd


def get_accessory(article):
    try:
        accessory = Accessory.objects.get(article=article)
    except Accessory.DoesNotExist:
        accessory = None
    return accessory


def get_series(series_id):
    try:
        series = Series.objects.get(id=series_id)
    except Series.DoesNotExist:
        series = None
    return series


def series_power_list(series_id):
    series = get_series(series_id)
    vfds = series.frequencydrive_set.all()
    powers = [(x.power, x.voltage) for x in vfds]
    return powers


def get_supplier(supplier_id):
    try:
        supplier = Supplier.objects.get(id=supplier_id)
    except Supplier.DoesNotExist:
        supplier = None
    return supplier


def get_price_vfd(supplier, vfd):
    try:
        price = Price.objects.filter(supplier=supplier, frequency_drive=vfd).first()
        return price
    except Price.DoesNotExist:
        return None

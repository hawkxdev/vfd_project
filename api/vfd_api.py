from vfd.models import FrequencyDrive, Accessory, Series


def get_vfd(article):
    try:
        vfd = FrequencyDrive.objects.get(article=article)
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

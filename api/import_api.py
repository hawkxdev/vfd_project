import pandas as pd

from api.vfd_api import get_vfd, get_accessory
from vfd.models import FrequencyDrive, Accessory, Price


def import_file(filename):
    df = pd.read_excel(filename, sheet_name=0)

    for i, row in df.iterrows():
        print(row)
        if row['type'] == 'vfd':
            add_vfd(row)
        elif row['type'] == 'accessory':
            pass
            # add_accessory(row)
        elif row['type'] == 'price':
            add_price(row)


def add_vfd(row):
    FrequencyDrive.objects.update_or_create(
        article=row['article'],
        defaults={
            'series_id': row['series_id'],
            'name': row['name'],
            'current': row['current'],
            'power': row['power'],
            'voltage': row['voltage'],
        }
    )


def add_accessory(row):
    for o in Accessory.objects.all():
        print(o.series.all())
    print()
    # Не делал, надо продумать как подтягивать из файла список серий


def add_price(row):
    frequency_drive = get_vfd(row['article'])
    accessory = None
    if not frequency_drive:
        accessory = get_accessory(row['article'])
    assert frequency_drive is not None or accessory is not None

    price = round(row['price without vat'], 2)
    Price.objects.update_or_create(
        frequency_drive=frequency_drive,
        accessory=accessory,
        supplier_id=row['supplier_id'],
        defaults={
            'price': price,
        }
    )

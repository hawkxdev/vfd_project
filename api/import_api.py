import pandas as pd

from vfd.models import FrequencyDrive, Accessory


def import_file(filename):
    df = pd.read_excel(filename, sheet_name=0)

    for i, row in df.iterrows():
        print(row)
        if row['type'] == 'vfd':
            add_vfd(row)
        elif row['type'] == 'accessory':
            pass
            # add_accessory(row)


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

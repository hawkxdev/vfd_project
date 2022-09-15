import math
from datetime import datetime
from math import floor
from PIL import Image, UnidentifiedImageError


def try_or(func, default=None, expected_exc=(Exception,)):
    try:
        return func()
    except expected_exc:
        return default


class MyTimer:
    def __init__(self):
        self.start_time = datetime.now()
        self.result = None

    def stop(self):
        self.result = datetime.now() - self.start_time
        self.result = f'Elapsed time: {format_timedelta(self.result)}'
        return self.result

    def result(self):
        return self.result


def format_timedelta(value, time_format="{hours2}:{minutes2}:{seconds2}"):
    if hasattr(value, 'seconds'):
        seconds = value.seconds + value.days * 24 * 3600
    else:
        seconds = int(value)

    seconds_total = seconds

    minutes = int(floor(seconds / 60))
    minutes_total = minutes
    seconds -= minutes * 60

    hours = int(floor(minutes / 60))
    hours_total = hours
    minutes -= hours * 60

    days = int(floor(hours / 24))
    days_total = days
    hours -= days * 24

    years = int(floor(days / 365))
    years_total = years
    days -= years * 365

    return time_format.format(**{
        'seconds': seconds,
        'seconds2': str(seconds).zfill(2),
        'minutes': minutes,
        'minutes2': str(minutes).zfill(2),
        'hours': hours,
        'hours2': str(hours).zfill(2),
        'days': days,
        'years': years,
        'seconds_total': seconds_total,
        'minutes_total': minutes_total,
        'hours_total': hours_total,
        'days_total': days_total,
        'years_total': years_total,
    })


def img_resize(*, img_path, new_img_path, width=None, height=None) -> bool:
    try:
        img = Image.open(img_path)

        if not width:
            k = height / img.height
            width = math.floor(img.width * k)

        img = img.resize((width, height), Image.NEAREST)
        img.save(new_img_path)
        return True
    except UnidentifiedImageError as e:
        return False

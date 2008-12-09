import datetime

from django.conf import settings
from django.utils.tzinfo import FixedOffset, LocalTimezone

from Sun import Sun


def get_sun_status(timestamp):
    if not timestamp.tzinfo:
        timestamp = timestamp.replace(tzinfo=LocalTimezone(timestamp))
    sunrise, sunset = get_rise_set_times(timestamp)
    morning_twilight, evening_twilight = get_twilight_times(timestamp)

    if morning_twilight < timestamp < evening_twilight:
        if sunrise < timestamp < sunset:
            return 'day'
        else:
            return 'twilight'
    else:
        return 'night'


def get_amount_of_sun(timestamp):
    if not timestamp.tzinfo:
        timestamp = timestamp.replace(tzinfo=LocalTimezone(timestamp))
    sunrise, sunset = get_rise_set_times(timestamp)
    sunrise += datetime.timedelta(hours=1)
    sunset -= datetime.timedelta(hours=1)
    morning_twilight, evening_twilight = get_twilight_times(timestamp)
    if morning_twilight < timestamp < evening_twilight:
        if sunrise < timestamp < sunset:
            return 1.0
        else:
            if morning_twilight < timestamp <= sunrise:
                morning_range = sunrise - morning_twilight
                return (timestamp - morning_twilight).seconds / float(morning_range.seconds)
            elif sunset < timestamp <= evening_twilight:
                evening_range = evening_twilight - sunset
                return (evening_range - (timestamp - sunset)).seconds / float(evening_range.seconds)
    else:
        return 0.0


def get_twilight_times(timestamp):
    s = Sun()
    hours = s.civilTwilight(timestamp.year, timestamp.month, timestamp.day, settings.LOCATION[1], settings.LOCATION[0])
    return get_times(hours, timestamp)


def get_rise_set_times(timestamp):
    s = Sun()
    hours = s.sunRiseSet(timestamp.year, timestamp.month, timestamp.day, settings.LOCATION[1], settings.LOCATION[0])
    return get_times(hours, timestamp)


def get_times(hours, timestamp):
    utc = FixedOffset(0)
    times = [datetime.time(int(t), int((t - int(t)) * 60), tzinfo=utc) for t in hours]
    localtz = LocalTimezone(timestamp)
    return [datetime.datetime.combine(timestamp.date(), t).astimezone(localtz) for t in times]

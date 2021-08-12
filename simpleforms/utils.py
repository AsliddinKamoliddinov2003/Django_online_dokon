from django.utils.timezone import  get_current_timezone
from datetime import datetime


def parse_date_time(date, time):
    time_str = f"{str(date)} {str(time)}"

    tz = get_current_timezone()
    dt = tz.localize(datetime.strptime(time_str, "%Y-%m-%d %H:%M"))

    return dt
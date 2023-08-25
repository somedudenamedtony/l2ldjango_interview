from django import template
import datetime

register = template.Library()


@register.filter
def l2l_dt(value):
    dt_format = "%Y-%m-%d %H:%M:%S"
    dt_str_format = "%Y-%m-%dT%H:%M:%S"

    if isinstance(value, datetime.datetime):
        return value.strftime(dt_format)

    if isinstance(value, str):
        dt = datetime.datetime.strptime(value, dt_str_format)
        return dt.strftime(dt_format)

    raise ValueError("Value must be a datetime or a string with the format " + dt_str_format)

from django import template
import datetime

register = template.Library()


@register.filter
def l2l_dt(value):
    dt_format = "%Y-%m-%d %H:%M:%S"
    dt_str_format = "%Y-%m-%dT%H:%M:%S"
    dt = value

    if not type(value) is str and not type(value) is datetime:
        raise ValueError("Value must be a datetime or a string with the format " + dt_str_format)

    if type(value) is str:
        dt = datetime.datetime.strptime(value, dt_str_format)

    return dt.strftime(dt_format)

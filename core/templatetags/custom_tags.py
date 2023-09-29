import datetime
from calendar import Calendar, HTMLCalendar

from django import template
from django.utils.safestring import mark_safe

from core.forms import CalendarForm

register = template.Library()


@register.filter(name='fav_model')
def fav_model(model):
    return True if model['name'] in ['Reservations', 'Chambres', 'Clients'] else False


@register.simple_tag(name="calendar")
def calendar():
    cal1 = HTMLCalendar(firstweekday=-1)
    today = datetime.date.today()
    return mark_safe(cal1.formatmonth(today.year,today.month))




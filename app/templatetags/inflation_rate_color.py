from django import template

register = template.Library()

@register.filter()
def first_or_last_el(value,number):
    return value[number]


@register.filter()
def el_months(value):
    return value[1:-1]

@register.filter()
def rate_color(value):
    if value == '-':
        value = 0
    if float(value) < 0:
        color = '#228526'
    elif 1 <= float(value) <= 2:
        color = '#faa5a5'
    elif 2 < float(value) <= 5:
        color = '#e34b5d'
    elif float(value) > 5:
        color = '#c2172b'
    else:
        color = 'White'
    return color





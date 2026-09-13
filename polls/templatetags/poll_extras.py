from django import template

register = template.Library()

@register.filter
def price_filter(value):
    return "{:,}".format(value) + ' ' + 'تومان'
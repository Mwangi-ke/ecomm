from django import template

register = template.Library()

@register.filter
def dict_key(value, arg):
    try:
        return value[arg]
    except KeyError:
        return None
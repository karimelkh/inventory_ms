from django import template

register = template.Library()

@register.filter(name="multiply")
def multiply(a, b):
    try:
        return a * b
    except (TypeError, ValueError):
        return None

from django import template

register = template.Library()

@register.filter
def get_dynamic_attr(obj, attr_name):
    """
    Custom template filter to dynamically access attributes of an object.
    """
    try:
        value = getattr(obj, attr_name)
        return str(value) if value is not None else ""
    except AttributeError:
        return None

@register.filter
def get_dict_item(dictionary, key):
    """
    Returns the value from a dictionary for the given key, or None if the key doesn't exist.
    """
    return dictionary.get(key)

@register.filter
def replace_underscore(value):
    return value.replace('_', ' ')

@register.filter
def explain_attr(dictionary, key):
    return dictionary.get(key, '')

@register.filter
def get_field_value(form, field_name):
    try:
        value = form.fields[field_name].value()
    except KeyError:
        value = None
    return value

@register.filter
def mul(value, arg):
    """Multiply the value by the argument."""
    try:
        return float(value or 0) * float(arg or 1)
    except (ValueError, TypeError):
        return 0
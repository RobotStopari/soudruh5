from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    if hasattr(field, 'field') and hasattr(field.field.widget, 'attrs'):
        existing_classes = field.field.widget.attrs.get('class', '')
        field.field.widget.attrs['class'] = f"{existing_classes} {css_class}".strip()
    return field

@register.filter(name='add_placeholder')
def add_placeholder(field, css_placeholder):
    if hasattr(field, 'field') and hasattr(field.field.widget, 'attrs'):
        existing_placeholders = field.field.widget.attrs.get('placeholder', '')
        field.field.widget.attrs['placeholder'] = f"{existing_placeholders} {css_placeholder}".strip()
    return field

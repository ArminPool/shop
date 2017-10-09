from django import template
register = template.Library()


@register.filter(name='persian_numeric')
def persian_numeric(value):

    length = len(value)
    for char in value:
        if char is '0':
            char = '۰'
            value += char
        elif char is '1':
            char = '۱'
            value += char
        elif char is '2':
            char = '۲'
            value += char
        elif char is '3':
            char = '۳'
            value += char
        elif char is '4':
            char = '۴'
            value += char
        elif char is '5':
            char = '۵'
            value += char
        elif char is '6':
            char = '۶'
            value += char
        elif char is '7':
            char = '۷'
            value += char
        elif char is '8':
            char = '۸'
            value += char
        elif char is '9':
            char = '۹'
            value += char
        else:
            value += char

    return value[length:]



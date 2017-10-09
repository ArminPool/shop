from django import template
register = template.Library()


@register.filter(name='persian_numeric')
def persian_numeric(value, arg):

    length = len(arg)
    for char in arg:
        if char is '0':
            char = '۰'
            arg += char
        elif char is '1':
            char = '۱'
            arg += char
        elif char is '2':
            char = '۲'
            arg += char
        elif char is '3':
            char = '۳'
            arg += char
        elif char is '4':
            char = '۴'
            arg += char
        elif char is '5':
            char = '۵'
            arg += char
        elif char is '6':
            char = '۶'
            arg += char
        elif char is '7':
            char = '۷'
            arg += char
        elif char is '8':
            char = '۸'
            arg += char
        elif char is '9':
            char = '۹'
            arg += char
        else:
            arg += char

    return arg[length:]



from django import template

register = template.Library()

def cut(value,arg):
    # this cuts all the values of the string from arg

    return value.replace(arg,'')
register.filter('cut',cut)  
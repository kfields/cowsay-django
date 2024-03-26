import cowsay
from django import template

register = template.Library()


@register.simple_tag
def cowsays(char="cow", text="Hello from Cowsay!"):
    return cowsay.get_output_string(char, text)

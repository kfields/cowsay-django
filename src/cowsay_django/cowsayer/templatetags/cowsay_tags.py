from django import template

import cowsay

register = template.Library()

@register.simple_tag
def cowsays(char="cow", text="Hello from Cowsay!"):
    return cowsay.get_output_string(char, text)

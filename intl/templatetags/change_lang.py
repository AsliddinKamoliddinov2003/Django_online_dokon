from django import template

register = template.Library()


@register.filter(name="change_lang")
def change_lang(request, lang):
    return "Salom"
from django import template

register = template.Library()


@register.filter(name="change_lang")
def change_lang(request, lang):
    url_parts = str(request.path).split('/')
    url_parts[1]=lang
    return "/".join(url_parts)
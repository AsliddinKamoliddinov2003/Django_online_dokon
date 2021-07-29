from django import template

register = template.Library()

@register.filter
def has_query_string(request):
    return bool(request.GET)
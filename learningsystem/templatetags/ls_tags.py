from django import template


register = template.Library()


@register.simple_tag
def query(qs, **kwargs):
    return qs.filter(**kwargs)

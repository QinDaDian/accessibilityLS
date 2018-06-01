from django import template


register = template.Library()


@register.simple_tag
def query(qs, **kwargs):
    return qs.filter(**kwargs)


@register.simple_tag
def result_exp(result):
    if result == 0:
        return '不通过'
    elif result == 1:
        return '通过'
    else:
        return '不存在'

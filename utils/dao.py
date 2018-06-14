from learningsystem.models import Item


def get_stdresult(page_id,rule_id):
    item = Item.objects.filter(page_id=page_id, rule_id=rule_id)
    if item:
        print(item)
        std_result = item[0].result
        text_reason = item[0].text_reason
    else:
        std_result = 2
        text_reason = '不存在'
    return std_result, text_reason
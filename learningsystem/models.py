from django.db import models

from accessibilityLS.baseModel import BaseModel


# Create your models here.
class Item(BaseModel):
    item_id = models.IntegerField('学习项id', primary_key=True, auto_created=True)
    page_id = models.IntegerField('网页id')


class Record(BaseModel):
    RESULT = (
        (0, '不通过'),
        (1, '通过'),
        (2, '不存在'),
        (3, '不知道')
    )
    JUDGE = (
        (0, '用户答案与标答不一致'),
        (1, '用户答案与标答一致')
    )
    record_id = models.IntegerField('学习记录id', primary_key=True, auto_created=True)
    item_id = models.IntegerField('学习项id')
    rule_id = models.IntegerField('规则id')
    user_id = models.IntegerField('用户id')
    user_result = models.IntegerField('用户答案', choices=RESULT)
    std_result = models.IntegerField('标准答案', choices=RESULT)
    judge = models.IntegerField('用户答案判断', choices=JUDGE)
    reason = models.TextField('用户给出的理由')
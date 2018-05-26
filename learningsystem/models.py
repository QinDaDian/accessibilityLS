from django.db import models
from django.utils.timezone import now

from accessibilityLS.baseModel import BaseModel


# Create your models here.
class Item(BaseModel):
    item_id = models.AutoField('学习项id', primary_key=True)
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
    # REASON_TAG = (
    #     (0, '手动填写'),
    #     (1, '上传图片')
    # )
    record_id = models.AutoField('学习记录id', primary_key=True)
    page_id = models.IntegerField('网页id', null=True)
    rule_id = models.IntegerField('规则id')
    user_id = models.IntegerField('用户id')
    user_result = models.IntegerField('用户答案', choices=RESULT)
    std_result = models.IntegerField('标准答案', choices=RESULT)
    judge = models.IntegerField('用户答案判断', choices=JUDGE)
    reason = models.TextField('用户给出的文本理由', null=True)
    reason_images=models.ImageField('用户上传的图片理由', blank=True, upload_to="upload")
    change_count=models.IntegerField('答案的切换次数', default=0)
    # reason_tag = models.IntegerField('填写理由的方式', choices=REASON_TAG, null=True)
    start_time = models.DateTimeField('申请任务的时间', default=now)
    finish_time = models.DateTimeField('任务结束的时间', default=now)

from django.db import models

from django.utils.timezone import now

from accessibilityLS.baseModel import BaseModel

class Examination(BaseModel):
    examination_id = models.AutoField('考卷主键', primary_key=True)
    user_id = models.IntegerField('用户id')
    question_num = models.IntegerField('考题个数')
    score = models.IntegerField('考卷总分数')
    start_time = models.DateTimeField('申请任务的时间', default=now)
    finish_time = models.DateTimeField('任务结束的时间', default=now)

class Question(BaseModel):
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
    question_id = models.AutoField('考题主键', primary_key=True)
    examination_id = models.IntegerField('考卷id')
    question_number = models.IntegerField('题号')
    page_id = models.IntegerField('网页id', null=True)
    rule_id = models.IntegerField('规则id')
    user_result = models.IntegerField('用户答案', choices=RESULT)
    std_result = models.IntegerField('标准答案', choices=RESULT)
    judge = models.IntegerField('用户答案判断', choices=JUDGE)
    reason = models.TextField('用户给出的文本理由', null=True)
    reason_images = models.ImageField('用户上传的图片理由', blank=True, upload_to="upload", null=True)
    std_reason = models.TextField('标准文本理由', null=True)
    change_count = models.IntegerField('答案的切换次数', default=0)
    start_time = models.DateTimeField('申请任务的时间', default=now)
    finish_time = models.DateTimeField('任务结束的时间', default=now)




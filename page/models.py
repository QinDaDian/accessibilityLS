from django.db import models

from accessibilityLS.baseModel import BaseModel


class Host(BaseModel):
    host_id = models.AutoField('网站id', primary_key=True)
    host_name = models.CharField('网站名称', max_length=255)
    host_domain = models.CharField('网站域名', max_length=255)


class Rule(BaseModel):
    IMPLEMENTED = (
        (0, '未实现'),
        (1, '已实现')
    )
    CHECK_TYPE = (
        (0, '未知'),
        (1, '自动检测'),
        (2, '半自动检测'),
        (3, '人工检测')
    )

    rule_id = models.AutoField('检测规则id', primary_key=True)
    standard = models.CharField('标准',  max_length=200)
    rule_doc_id = models.CharField('规则编号', max_length=50)
    title = models.CharField('规则名', max_length=100)
    implemented = models.IntegerField('规则是否被实现', choices=IMPLEMENTED)
    level = models.IntegerField('等级')
    type = models.IntegerField('类型', choices=CHECK_TYPE)
    difficulty = models.IntegerField('难度等级')
    description = models.TextField('规则说明', null=True)
    check_method = models.TextField('检测方法说明', null=True)
    pass_condition = models.TextField('通过条件说明', null=True)
    freq_ans = models.TextField('不通过的常规答案', null=True)


class Page(BaseModel):
    page_id = models.AutoField('网页id', primary_key=True)
    host_id = models.IntegerField('网站id')
    local_dir = models.CharField('本地地址', max_length=255, null=True, blank=True)
    url = models.CharField('url', max_length=4096)
    depth = models.IntegerField('网页所在层数')
    title = models.CharField('网页标题', max_length=255)
    encode = models.CharField('网页编码', max_length=16)
    x_frame_options = models.CharField('iframe加载问题', max_length=255, null=True, blank=True)






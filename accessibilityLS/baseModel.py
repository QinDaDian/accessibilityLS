from django.db import models

from django.utils.timezone import now


# base model of the whole system
class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', default = now)
    modify_time = models.DateTimeField('修改时间', default = now)

    class Meta:
        abstract = True
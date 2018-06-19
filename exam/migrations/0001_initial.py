# Generated by Django 2.0.4 on 2018-06-12 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('examination_id', models.AutoField(primary_key=True, serialize=False, verbose_name='考卷主键')),
                ('user_id', models.IntegerField(verbose_name='用户id')),
                ('question_num', models.IntegerField(verbose_name='考题个数')),
                ('score', models.IntegerField(verbose_name='考卷总分数')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='申请任务的时间')),
                ('finish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='任务结束的时间')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('modify_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间')),
                ('question_id', models.AutoField(primary_key=True, serialize=False, verbose_name='考题主键')),
                ('examination_id', models.IntegerField(verbose_name='考卷id')),
                ('question_number', models.IntegerField(verbose_name='题号')),
                ('page_id', models.IntegerField(null=True, verbose_name='网页id')),
                ('rule_id', models.IntegerField(verbose_name='规则id')),
                ('user_result', models.IntegerField(choices=[(0, '不通过'), (1, '通过'), (2, '不存在'), (3, '不知道')], verbose_name='用户答案')),
                ('std_result', models.IntegerField(choices=[(0, '不通过'), (1, '通过'), (2, '不存在'), (3, '不知道')], verbose_name='标准答案')),
                ('judge', models.IntegerField(choices=[(0, '用户答案与标答不一致'), (1, '用户答案与标答一致')], verbose_name='用户答案判断')),
                ('reason', models.TextField(null=True, verbose_name='用户给出的文本理由')),
                ('reason_images', models.ImageField(blank=True, null=True, upload_to='upload', verbose_name='用户上传的图片理由')),
                ('change_count', models.IntegerField(default=0, verbose_name='答案的切换次数')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='申请任务的时间')),
                ('finish_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='任务结束的时间')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
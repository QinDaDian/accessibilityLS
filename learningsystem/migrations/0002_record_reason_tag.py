# Generated by Django 2.0.3 on 2018-04-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningsystem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='reason_tag',
            field=models.IntegerField(choices=[(0, '手动填写'), (1, '自动获取')], null=True, verbose_name='填写理由的方式'),
        ),
    ]
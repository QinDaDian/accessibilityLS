# Generated by Django 2.0.3 on 2018-04-29 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningsystem', '0002_record_reason_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='学习项id'),
        ),
        migrations.AlterField(
            model_name='record',
            name='record_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='学习记录id'),
        ),
    ]

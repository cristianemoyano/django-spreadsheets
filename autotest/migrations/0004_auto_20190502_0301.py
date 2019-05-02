# Generated by Django 2.2.1 on 2019-05-02 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotest', '0003_auto_20190502_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='responses',
            name='key_max_first',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='responses',
            name='key_max_second',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='responses',
            name='percent_max_first',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='responses',
            name='percent_max_second',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='responses',
            name='val_max_first',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='responses',
            name='val_max_second',
            field=models.IntegerField(default=0),
        ),
    ]

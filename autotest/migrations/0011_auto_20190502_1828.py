# Generated by Django 2.2.1 on 2019-05-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotest', '0010_datafile_key_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datafile',
            name='key_file',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
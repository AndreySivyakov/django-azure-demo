# Generated by Django 2.2.6 on 2019-11-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_auto_20191114_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='resolution',
            field=models.CharField(default='', max_length=100),
        ),
    ]

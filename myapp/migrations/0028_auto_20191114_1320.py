# Generated by Django 2.2.6 on 2019-11-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20191114_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='resolution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

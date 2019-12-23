# Generated by Django 2.2.5 on 2019-10-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20191031_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_number', models.BigIntegerField(null=True)),
                ('vendor_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Claim',
        ),
    ]

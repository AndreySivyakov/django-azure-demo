# Generated by Django 2.2.5 on 2019-10-31 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_vendor_vendor_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]

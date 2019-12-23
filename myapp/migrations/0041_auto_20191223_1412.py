# Generated by Django 2.1.15 on 2019-12-23 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_auto_20191223_1345'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='claim',
            name='bus_unit',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='claim_type',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='close_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='contract',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='estimated_value',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='initiated_by',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='nature',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='open_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='original_value',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='po',
            field=models.BigIntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='projects',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='resolution',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='claim',
            name='responsible_rep',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_claim_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Claim'),
        ),
    ]

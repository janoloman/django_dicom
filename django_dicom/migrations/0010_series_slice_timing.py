# Generated by Django 2.1.5 on 2019-02-12 13:34

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dicom', '0009_auto_20190211_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='slice_timing',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]), blank=True, null=True, size=None),
        ),
    ]
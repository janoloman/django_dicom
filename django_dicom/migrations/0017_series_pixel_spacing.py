# Generated by Django 2.1.4 on 2019-02-14 08:08

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dicom', '0016_auto_20190213_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='pixel_spacing',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]), blank=True, help_text='Physical distance in the patient between the center of each pixel, specified by a numeric pair - adjacent row spacing (delimiter) adjacent column spacing in mm. See Section 10.7.1.3 for further explanation.', null=True, size=2),
        ),
    ]
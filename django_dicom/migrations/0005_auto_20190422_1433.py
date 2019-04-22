# Generated by Django 2.2 on 2019-04-22 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_dicom', '0004_auto_20190422_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Image Number'),
        ),
        migrations.AlterField(
            model_name='image',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2 on 2019-04-22 14:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('django_dicom', '0003_auto_20190422_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Image Number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='django_dicom.Series'),
        ),
        migrations.AlterField(
            model_name='image',
            name='time',
            field=models.TimeField(),
        ),
    ]

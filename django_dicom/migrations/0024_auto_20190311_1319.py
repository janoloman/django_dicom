# Generated by Django 2.1.5 on 2019-03-11 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_dicom', '0023_auto_20190311_1137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='manufacturers_model_name',
            new_name='manufacturer_model_name',
        ),
    ]
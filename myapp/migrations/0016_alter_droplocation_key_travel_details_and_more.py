# Generated by Django 5.1.2 on 2024-12-06 15:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_droplocation_key_travel_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='droplocation',
            name='Key_Travel_Details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='droplocation',
            name='place_visit',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

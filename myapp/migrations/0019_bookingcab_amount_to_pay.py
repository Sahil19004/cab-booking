# Generated by Django 5.1.2 on 2024-12-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_carstype_toll_tax'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingcab',
            name='amount_to_pay',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2024-02-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petboarding', '0021_boardingform_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('boarduser', 'Boarduser'), ('taker', 'Taker'), ('admin', 'Admin')], default='admin', max_length=20),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petboarding', '0005_boardingform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardingform',
            name='enddate',
            field=models.DateField(),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-21 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petboarding', '0007_alter_boardingform_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardingform',
            name='nuberofpetboarded',
            field=models.CharField(max_length=20),
        ),
    ]

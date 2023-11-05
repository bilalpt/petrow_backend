# Generated by Django 4.2.7 on 2023-11-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petboarding', '0008_alter_boardingform_nuberofpetboarded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('boarduser', 'Boarduser'), ('taker', 'Taker'), ('admin', 'Admin')], default='admin', max_length=20),
        ),
    ]

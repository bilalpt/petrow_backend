# Generated by Django 4.2.7 on 2023-11-05 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petboarding', '0011_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('boarduser', 'Boarduser'), ('taker', 'Taker'), ('admin', 'Admin')], default='boarduser', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]

# Generated by Django 4.2.7 on 2024-01-01 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petboarding', '0019_user_accepttaker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='accepttaker',
        ),
    ]

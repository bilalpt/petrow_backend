# Generated by Django 4.2.5 on 2023-10-22 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petcare', '0003_rename_enjoyment_or_takerabotpage_skillandqualifications_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='takerabotpage',
            old_name='indroduction',
            new_name='introduction',
        ),
    ]
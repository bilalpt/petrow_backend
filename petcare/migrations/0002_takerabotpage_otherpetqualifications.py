# Generated by Django 4.2.5 on 2023-10-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='takerabotpage',
            name='otherpetqualifications',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

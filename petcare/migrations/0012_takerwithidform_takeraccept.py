# Generated by Django 4.2.7 on 2024-01-01 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petcare', '0011_alter_describeservicetwo_pincode'),
    ]

    operations = [
        migrations.AddField(
            model_name='takerwithidform',
            name='Takeraccept',
            field=models.BooleanField(default=False),
        ),
    ]
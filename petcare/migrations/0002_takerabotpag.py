# Generated by Django 4.2.7 on 2023-11-05 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('petcare', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakerAbotpag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction', models.CharField(max_length=255)),
                ('petexperience', models.CharField(max_length=255)),
                ('workstatus', models.CharField(max_length=255)),
                ('skillandqualifications', models.CharField(max_length=255)),
                ('otherpetqualifications', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
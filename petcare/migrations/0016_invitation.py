# Generated by Django 4.2.7 on 2024-01-13 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petboarding', '0021_boardingform_pincode'),
        ('petcare', '0015_delete_invitation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('request', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petcare.takerwithidform')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petboarding.boardingform')),
            ],
        ),
    ]

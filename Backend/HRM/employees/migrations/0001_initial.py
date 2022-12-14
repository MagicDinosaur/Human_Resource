# Generated by Django 4.1.4 on 2023-01-02 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('profile_pic', models.CharField(max_length=800)),
                ('resume', models.FileField(blank=True, upload_to='resume')),
                ('position', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('salary', models.CharField(max_length=200)),
                ('date_hired', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_view_employee', 'Can view employee'), ('can_add_employee', 'Can add employee'), ('can_change_employee', 'Can change employee'), ('can_delete_employee', 'Can delete employee')),
            },
        ),
    ]

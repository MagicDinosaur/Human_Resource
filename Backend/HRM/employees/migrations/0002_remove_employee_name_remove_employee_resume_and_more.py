# Generated by Django 4.1.4 on 2023-01-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='resume',
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(choices=[('IT', 'IT'), ('HR', 'HR'), ('Sales', 'Sales'), ('Marketing', 'Marketing'), ('Finance', 'Finance'), ('Operations', 'Operations'), ('Others', 'Others')], max_length=200),
        ),
    ]

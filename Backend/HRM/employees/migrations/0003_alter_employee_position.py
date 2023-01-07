# Generated by Django 4.1.4 on 2023-01-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_remove_employee_name_remove_employee_resume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('CEO', 'CEO'), ('Manager', 'Manager'), ('Senior', 'Senior'), ('Junior', 'Junior'), ('Trainee', 'Trainee'), ('Others', 'Others')], default='Others', max_length=200),
        ),
    ]

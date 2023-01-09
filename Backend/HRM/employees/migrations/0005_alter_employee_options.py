# Generated by Django 4.1.4 on 2023-01-04 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employee_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'default_permissions': 'view', 'permissions': (('can_view_employee', 'Can view employee'), ('can_add_employee', 'Can add employee'), ('can_change_employee', 'Can change employee'), ('can_delete_employee', 'Can delete employee'))},
        ),
    ]
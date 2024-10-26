# Generated by Django 5.0.4 on 2024-10-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_superadmin_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('CLIENT', 'client'), ('AGENT', 'agent'), ('ADMIN', 'admin'), ('SUPERUSER', 'superuser')], default='', max_length=32),
        ),
    ]

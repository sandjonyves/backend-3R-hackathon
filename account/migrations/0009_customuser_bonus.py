# Generated by Django 5.0.4 on 2024-10-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_customuser_latitude_customuser_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bonus',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]

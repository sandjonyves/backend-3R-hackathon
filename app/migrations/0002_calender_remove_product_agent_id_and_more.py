# Generated by Django 5.0.4 on 2024-10-25 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_customuser_bonus'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='calender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kwattar', models.CharField(max_length=255)),
                ('days', models.CharField(max_length=255)),
                ('hours', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='Agent_id',
        ),
        migrations.RemoveField(
            model_name='thums',
            name='Product_id',
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passing_date', models.DateField(auto_created=True, null=True)),
                ('agent_id', models.IntegerField()),
                ('client_ids', models.ManyToManyField(to='account.client')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionAdmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_subscribe', models.DateField(auto_now_add=True)),
                ('end_subscribe', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.admin')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.IntegerField()),
                ('start_subscribe', models.DateField(auto_now_add=True)),
                ('end_subscribe', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('client_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.client')),
            ],
        ),
        migrations.DeleteModel(
            name='Commande',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Thums',
        ),
    ]
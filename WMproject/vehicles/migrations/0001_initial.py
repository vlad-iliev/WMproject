# Generated by Django 3.2.16 on 2022-12-13 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_consumption', models.PositiveIntegerField()),
                ('fuel_tank_capacity', models.PositiveIntegerField()),
                ('small_service_cost', models.PositiveIntegerField(default=100)),
                ('medium_service_cost', models.PositiveIntegerField(default=250)),
                ('major_service_cost', models.PositiveIntegerField(default=500)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('maintenance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.maintenance')),
                ('reg_number', models.TextField(max_length=7)),
                ('make', models.TextField(max_length=30)),
                ('model', models.TextField(max_length=30)),
                ('year', models.PositiveIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('colour', models.TextField(max_length=20)),
                ('license_category', models.TextField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('vehicles.maintenance', models.Model),
        ),
        migrations.CreateModel(
            name='Van',
            fields=[
                ('maintenance_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='vehicles.maintenance')),
                ('reg_number', models.TextField(max_length=7)),
                ('make', models.TextField(max_length=30)),
                ('model', models.TextField(max_length=30)),
                ('year', models.PositiveIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('colour', models.TextField(max_length=20)),
                ('license_category', models.TextField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('vehicles.maintenance', models.Model),
        ),
    ]
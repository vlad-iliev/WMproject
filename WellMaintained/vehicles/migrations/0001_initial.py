# Generated by Django 3.2.16 on 2022-12-17 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Van',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.TextField(max_length=8, unique=True)),
                ('make', models.TextField(max_length=30)),
                ('model', models.TextField(max_length=30)),
                ('year', models.PositiveIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('colour', models.TextField(max_length=20)),
                ('license_category', models.TextField(max_length=20)),
                ('auto_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.autopark')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_number', models.TextField(max_length=8, unique=True)),
                ('make', models.TextField(max_length=30)),
                ('model', models.TextField(max_length=30)),
                ('year', models.PositiveIntegerField()),
                ('mileage', models.PositiveIntegerField()),
                ('colour', models.TextField(max_length=20)),
                ('license_category', models.TextField(max_length=20)),
                ('auto_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.autopark')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
# Generated by Django 3.2.16 on 2022-12-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
        ('accounts', '0002_alter_profile_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='hired_cars',
            field=models.ManyToManyField(blank=True, null=True, to='vehicles.Car'),
        ),
    ]

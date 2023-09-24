# Generated by Django 4.2.5 on 2023-09-24 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emissionrecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_value', models.FloatField()),
                ('record_year', models.IntegerField()),
                ('net_emission', models.FloatField()),
            ],
            options={
                'db_table': 'emissionrecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'factor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'organization',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subfactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'subfactor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subsubfactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('emission_factor', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('unit', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'subsubfactor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip', models.TextField()),
                ('potential_reduction_percentage', models.FloatField()),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.factor')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-23 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SubFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.factor')),
            ],
        ),
        migrations.CreateModel(
            name='SubSubFactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('emission_factor', models.FloatField()),
                ('sub_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subfactor')),
            ],
        ),
        migrations.CreateModel(
            name='EmissionRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_value', models.FloatField()),
                ('record_year', models.IntegerField()),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.organisation')),
                ('sub_sub_factor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.subsubfactor')),
            ],
        ),
    ]

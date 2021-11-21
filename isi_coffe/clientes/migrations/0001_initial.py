# Generated by Django 3.1.5 on 2021-11-20 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=255)),
                ('municipio', models.CharField(max_length=255)),
                ('colonia', models.CharField(max_length=255)),
                ('codigo_postal', models.PositiveSmallIntegerField()),
                ('calle', models.CharField(max_length=255)),
                ('numero_exterior', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tarjetas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
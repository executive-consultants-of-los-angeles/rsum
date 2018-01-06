# Generated by Django 2.0.1 on 2018-01-06 06:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('content', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='section', max_length=200)),
                ('content', django.contrib.postgres.fields.jsonb.JSONField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Profile')),
            ],
        ),
    ]

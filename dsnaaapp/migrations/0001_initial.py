# Generated by Django 3.2.4 on 2021-06-24 14:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('mdp', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('dateCreation', models.DateTimeField(verbose_name=datetime.datetime(2021, 6, 24, 15, 44, 32, 309078))),
                ('dateUpdate', models.DateTimeField(verbose_name=datetime.datetime(2021, 6, 24, 15, 44, 32, 309078))),
                ('autheur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsnaaapp.admin')),
            ],
        ),
    ]

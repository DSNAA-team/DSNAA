# Generated by Django 3.2.4 on 2021-08-13 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dsnaaapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='gallery',
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dsnaaapp.album'),
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]

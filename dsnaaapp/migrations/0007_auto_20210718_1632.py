# Generated by Django 3.2.4 on 2021-07-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsnaaapp', '0006_auto_20210718_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='mediacategory',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
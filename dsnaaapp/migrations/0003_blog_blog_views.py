# Generated by Django 3.2.4 on 2021-07-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsnaaapp', '0002_alter_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_views',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-29 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dsnaaapp', '0004_auto_20210629_1303'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.TextField(max_length=50)),
                ('firstname', models.TextField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('subject', models.TextField(max_length=255)),
                ('message', models.TextField(max_length=350)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('titre', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VideoLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.TextField(max_length=255)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('theme', models.TextField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.TextField(max_length=255)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('organisation', models.TextField(max_length=40)),
                ('longueur', models.FloatField()),
                ('description', models.TextField(max_length=255)),
                ('lien', models.TextField(max_length=100)),
                ('videoLibrary', models.ManyToManyField(to='dsnaaapp.VideoLibrary')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=500)),
                ('date_publication', models.DateTimeField(auto_now_add=True)),
                ('lieu', models.TextField(max_length=40)),
                ('image', models.ImageField(upload_to='')),
                ('gallery', models.ManyToManyField(to='dsnaaapp.Gallery')),
            ],
        ),
    ]

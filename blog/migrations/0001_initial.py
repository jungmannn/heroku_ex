# Generated by Django 2.2.3 on 2019-07-27 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=20)),
                ('rating', models.CharField(max_length=20)),
                ('notice', models.CharField(max_length=20)),
                ('save_date', models.DateTimeField(verbose_name='Movie Release date')),
                ('image', models.ImageField(upload_to='image/')),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

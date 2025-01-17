# Generated by Django 4.0.5 on 2022-06-02 17:01

from django.db import migrations, models
import django.db.models.deletion
import photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directories', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(upload_to='photos/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_dir', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to=photos.models.upload_function)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.feed')),
            ],
        ),
    ]

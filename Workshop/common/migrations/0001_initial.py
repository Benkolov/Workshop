# Generated by Django 5.0.4 on 2024-05-11 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('photos', '0006_alter_photo_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('publication_date_and_time', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='photos.photo')),
            ],
        ),
    ]

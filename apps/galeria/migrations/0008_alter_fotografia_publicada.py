# Generated by Django 5.1.5 on 2025-03-11 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0007_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]

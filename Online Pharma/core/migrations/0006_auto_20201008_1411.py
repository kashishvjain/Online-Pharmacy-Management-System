# Generated by Django 3.0.3 on 2020-10-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201008_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='slug',
            field=models.SlugField(default=1, unique=True),
        ),
    ]

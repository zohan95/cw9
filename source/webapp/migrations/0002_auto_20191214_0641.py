# Generated by Django 2.2 on 2019-12-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Фотография'),
        ),
    ]

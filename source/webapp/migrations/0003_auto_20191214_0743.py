# Generated by Django 2.2 on 2019-12-14 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0002_auto_20191214_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='photo_user',
                                    to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]

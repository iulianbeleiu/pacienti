# Generated by Django 2.2.12 on 2020-05-27 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pacient', '0003_auto_20200527_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='pacient',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Doctor'),
        ),
    ]
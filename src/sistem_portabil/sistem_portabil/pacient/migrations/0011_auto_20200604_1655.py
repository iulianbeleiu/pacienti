# Generated by Django 2.2.13 on 2020-06-04 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0010_delete_adresapacient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='user_pacient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_pacient', to=settings.AUTH_USER_MODEL),
        ),
    ]

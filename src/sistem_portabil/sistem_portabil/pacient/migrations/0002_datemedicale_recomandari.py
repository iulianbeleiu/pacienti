# Generated by Django 2.2.12 on 2020-05-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateMedicale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('istoric_medical', models.TextField(blank=True, default='', null=True)),
                ('alergii', models.TextField(blank=True, default='', null=True)),
                ('consultatii_cardiologice', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recomandari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tip_recomandare', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('durata_zilnica', models.IntegerField()),
                ('alte_indicatii', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]

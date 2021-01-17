# Generated by Django 2.2.12 on 2020-05-27 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0002_datemedicale_recomandari'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tara', models.CharField(max_length=200)),
                ('judet', models.CharField(max_length=200)),
                ('localitate', models.CharField(max_length=200)),
                ('strada', models.CharField(max_length=200)),
                ('scara', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('numar', models.CharField(max_length=200)),
                ('apartament', models.CharField(blank=True, default='', max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='pacient',
            name='date_medicale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pacient.DateMedicale'),
        ),
        migrations.AddField(
            model_name='pacient',
            name='recomandari',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pacient.Recomandari'),
        ),
        migrations.AddField(
            model_name='pacient',
            name='adresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pacient.Adresa'),
        ),
    ]
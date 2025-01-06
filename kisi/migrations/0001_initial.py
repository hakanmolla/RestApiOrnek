# Generated by Django 5.1.4 on 2025-01-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kisiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adi', models.CharField(max_length=100)),
                ('soyadı', models.CharField(max_length=100)),
                ('memleketi', models.CharField(max_length=100)),
                ('ulkesi', models.CharField(max_length=100)),
                ('tcno', models.DecimalField(decimal_places=0, max_digits=11)),
                ('olusturma_zamani', models.DateTimeField(auto_now_add=True)),
                ('guncelleme_zamani', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

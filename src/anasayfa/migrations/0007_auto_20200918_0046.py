# Generated by Django 3.1.1 on 2020-09-17 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0006_auto_20200918_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='totalmodel',
            options={'ordering': ['total'], 'verbose_name': 'Toplam Kahve Sayısı', 'verbose_name_plural': 'Toplam Kahve Sayısı'},
        ),
    ]

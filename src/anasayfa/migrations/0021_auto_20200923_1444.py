# Generated by Django 3.1.1 on 2020-09-23 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0020_auto_20200923_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kahveagacimodel',
            options={'ordering': ['title'], 'verbose_name': 'Yeşil kutu Açıklaması', 'verbose_name_plural': 'Yeşil kutu Açıklaması'},
        ),
        migrations.AlterModelOptions(
            name='kahvesayisimodel',
            options={'ordering': ['title'], 'verbose_name': 'Satılan Kahve Sayısı ', 'verbose_name_plural': 'SatılanKahve Sayısı'},
        ),
        migrations.AlterModelOptions(
            name='kahveyardimmodel',
            options={'ordering': ['tipname'], 'verbose_name': 'Ağaca kahve ekleyenler', 'verbose_name_plural': 'Ağaca kahve ekleyenler'},
        ),
        migrations.AlterModelOptions(
            name='totaltreemodel',
            options={'ordering': ['totalcofee'], 'verbose_name': 'Toplam Ağaçdaki  kahve Sayısı', 'verbose_name_plural': 'Toplam Ağaçtaki Kahve Sayısı'},
        ),
        migrations.AlterModelOptions(
            name='yardımsayisimodel',
            options={'ordering': ['title'], 'verbose_name': 'Turuncu kutu Açıklaması', 'verbose_name_plural': 'Turuncu kutu Açıklaması'},
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-23 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0024_auto_20200923_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kahvesayisimodel',
            options={'ordering': ['title'], 'verbose_name': 'Bugün satılan kahve Sayısı ', 'verbose_name_plural': 'Turun kutu satılan kahve Sayısı'},
        ),
    ]

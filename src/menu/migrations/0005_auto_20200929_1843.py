# Generated by Django 3.1.1 on 2020-09-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20200919_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='fiyat',
            field=models.CharField(blank=True, max_length=10, verbose_name='Fiyat Ekleyin'),
        ),
    ]
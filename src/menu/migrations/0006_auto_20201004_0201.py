# Generated by Django 3.1.1 on 2020-10-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20200929_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodel',
            name='bölüm',
            field=models.CharField(choices=[('kahveler', 'COFFEE BASED'), ('turkkahveleri', 'TÜRK KAHVESİ'), ('hotdrinks', 'HOT DRİNKS'), ('icedrinks', 'SOĞUK İÇECEKLER'), ('milhshake', 'MILK SHAKELER'), ('waffle', 'WAFFLE')], default='kahveler', max_length=30),
        ),
    ]

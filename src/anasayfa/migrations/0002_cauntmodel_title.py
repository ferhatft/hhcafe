# Generated by Django 3.1.1 on 2020-09-17 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cauntmodel',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Başlık'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hakkımızda', '0003_auto_20200918_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf Ekleyin'),
        ),
    ]

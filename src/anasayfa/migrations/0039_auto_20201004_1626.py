# Generated by Django 3.1.1 on 2020-10-04 13:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0038_auto_20201004_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='kahveagacimodel',
            name='imagetudent',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Öğrenci Fotoğraf Ekleyin'),
        ),
        migrations.AlterField(
            model_name='kahveagacimodel',
            name='pragrafstudent',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Öğrenci ağacı Açıklama'),
        ),
    ]

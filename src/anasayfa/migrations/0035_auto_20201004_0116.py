# Generated by Django 3.1.1 on 2020-10-03 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0034_auto_20200928_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kahveagacimodel',
            name='subtitledoctor',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Sağlık Çalışanı Ağacı Alt Başlık '),
        ),
        migrations.AlterField(
            model_name='kahveagacimodel',
            name='subtitlestudent',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Öğrenci ağacı Alt Başlık '),
        ),
        migrations.AlterField(
            model_name='kahvesayisimodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, verbose_name='Alt Başlık Ekleyin'),
        ),
        migrations.AlterField(
            model_name='yardımsayisimodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, verbose_name='Alt Başlık Ekleyin'),
        ),
    ]

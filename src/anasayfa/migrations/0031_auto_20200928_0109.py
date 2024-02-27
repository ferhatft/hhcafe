# Generated by Django 3.1.1 on 2020-09-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0030_auto_20200928_0051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kahveagacimodel',
            options={'ordering': ['id'], 'verbose_name': 'Yeşil kutu Açıklamaları', 'verbose_name_plural': 'Yeşil kutu Açıklamaları'},
        ),
        migrations.RemoveField(
            model_name='kahveagacimodel',
            name='pragraf',
        ),
        migrations.RemoveField(
            model_name='kahveagacimodel',
            name='slogan',
        ),
        migrations.RemoveField(
            model_name='kahveagacimodel',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='kahveagacimodel',
            name='title',
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='pragrafdoctor',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Sağlık Çalışanı Ağacı Açıklama '),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='pragrafstudent',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Öğrenci ağacı Açıklama '),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='slogandoctor',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Sağlık Çalışanı Ağacı Slogan '),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='sloganstudent',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Öğrenci ağacı Slogan '),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='subtitledoctor',
            field=models.CharField(max_length=500, null=True, verbose_name='Sağlık Çalışanı Ağacı Alt Başlık '),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='subtitlestudent',
            field=models.CharField(max_length=500, null=True, verbose_name='Öğrenci ağacı Alt Başlık '),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='titledoctor',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Sağlık Çalışanı Ağacı Başlık '),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='titlestudent',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Öğrenci Ağacı Başlığı'),
        ),
    ]

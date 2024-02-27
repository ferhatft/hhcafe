# Generated by Django 3.1.1 on 2020-09-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WinersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Başlık Ekleyin')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf Ekleyin')),
                ('wintime', models.DateTimeField(verbose_name='Tarih Ekleyin')),
            ],
            options={
                'verbose_name': 'Çekiliş Kazananları',
                'verbose_name_plural': 'Çekiliş Kazananları',
                'ordering': ['name'],
            },
        ),
    ]
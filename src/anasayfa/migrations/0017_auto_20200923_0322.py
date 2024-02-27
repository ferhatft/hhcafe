# Generated by Django 3.1.1 on 2020-09-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0016_auto_20200920_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='kahveagacimodel',
            name='tipname',
            field=models.CharField(blank=True, max_length=30, verbose_name='Yardım edenin ismi'),
        ),
        migrations.AddField(
            model_name='kahveagacimodel',
            name='tipnote',
            field=models.CharField(max_length=500, null=True, verbose_name='Yardım edenin notu'),
        ),
    ]

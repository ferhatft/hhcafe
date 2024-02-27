# Generated by Django 3.1.1 on 2020-09-28 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partnerlerimiz', '0003_auto_20200919_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnermodel',
            name='contextSubtitle',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Açıklama Alt Başlık Ekleyin'),
        ),
        migrations.AddField(
            model_name='partnermodel',
            name='contextparagraf',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Açıklama Paragrafı  Ekleyin'),
        ),
        migrations.AddField(
            model_name='partnermodel',
            name='contextslogan',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Açıklama Slogan Ekleyin'),
        ),
        migrations.AddField(
            model_name='partnermodel',
            name='contexttitle',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Açıklama Başlık Ekleyin'),
        ),
    ]
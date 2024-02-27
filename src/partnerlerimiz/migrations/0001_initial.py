# Generated by Django 3.1.1 on 2020-09-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartnerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='İsim Ekleyin')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='Fotoğraf Ekleyin')),
                ('facebook', models.CharField(blank=True, max_length=15, null=True, verbose_name='İsim Ekleyin')),
                ('instagram', models.CharField(blank=True, max_length=15, null=True, verbose_name='İsim Ekleyin')),
                ('linkedin', models.CharField(blank=True, max_length=15, null=True, verbose_name='İsim Ekleyin')),
                ('tweetter', models.CharField(blank=True, max_length=15, null=True, verbose_name='İsim Ekleyin')),
                ('alan', models.CharField(blank=True, max_length=15, null=True, verbose_name='İsim Ekleyin')),
            ],
            options={
                'verbose_name': 'Partnerlerimiz',
                'verbose_name_plural': 'Partnerlerimiz',
                'ordering': ['name'],
            },
        ),
    ]
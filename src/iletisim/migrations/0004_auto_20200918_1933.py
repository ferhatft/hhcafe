# Generated by Django 3.1.1 on 2020-09-18 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0003_contact_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['name'], 'verbose_name': 'Müşteri İletişim Bilgileri', 'verbose_name_plural': 'Müşteri İletişim Bilgileri'},
        ),
        migrations.AlterModelOptions(
            name='i̇nfo',
            options={'ordering': ['email'], 'verbose_name': 'Kafe İletişim Bilgileri', 'verbose_name_plural': 'Kafe İletişim Bilgileri'},
        ),
    ]

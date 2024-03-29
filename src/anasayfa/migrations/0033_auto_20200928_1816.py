# Generated by Django 3.1.1 on 2020-09-28 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anasayfa', '0032_auto_20200928_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='greeenboxmodel',
            options={'ordering': ['first'], 'verbose_name': 'Yeşil kutu üzrindeki yazılar', 'verbose_name_plural': 'Yeşil kutu üzrindeki yazılar'},
        ),
        migrations.AlterModelOptions(
            name='kahvedoctoryardimmodel',
            options={'ordering': ['name'], 'verbose_name': 'Yeşil Kutu Eklenen kahve (doktor)', 'verbose_name_plural': 'Yeşil Kutu Eklenen kahveler (doktor)'},
        ),
        migrations.AlterModelOptions(
            name='kahvestudentyardimmodel',
            options={'ordering': ['name'], 'verbose_name': 'Yeşil Kutu Eklenen kahve ( Öğrenci )', 'verbose_name_plural': 'Yeşil Kutu Eklenen kahveler ( Öğrenci )'},
        ),
        migrations.AlterModelOptions(
            name='orangeboxmodel',
            options={'ordering': ['first'], 'verbose_name': 'Turuncu kutu üzrindeki yazılar', 'verbose_name_plural': 'Turuncu kutu üzrindeki yazılar'},
        ),
        migrations.AlterModelOptions(
            name='pilregistermodel',
            options={'ordering': ['created_date'], 'verbose_name': 'Kırmızı Kutu Fiş Kayıtı', 'verbose_name_plural': 'Kırmızı Kutu Fiş Kayıtları'},
        ),
        migrations.AlterModelOptions(
            name='redboxmodel',
            options={'ordering': ['first'], 'verbose_name': 'Kırmızı kutu üzrindeki yazılar', 'verbose_name_plural': 'Kırmızı kutu üzrindeki yazılar'},
        ),
        migrations.AlterModelOptions(
            name='totalmodel',
            options={'ordering': ['total'], 'verbose_name': 'Günlük satılan kahve Sayısı', 'verbose_name_plural': 'Günlük satılan Kahve Sayısı'},
        ),
        migrations.AlterModelOptions(
            name='totaltreemodel',
            options={'ordering': ['id'], 'verbose_name': 'Yeşil Kutu Toplam Ağaçdaki  kahve Sayıları', 'verbose_name_plural': 'Yeşil Kutu Toplam Ağaçtaki Kahve Sayıları'},
        ),
    ]

# Generated by Django 3.1.1 on 2020-09-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iletisim', '0002_auto_20200918_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=25, null=True),
        ),
    ]

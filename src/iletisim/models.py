from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

STATUS = (
    ('new', 'New'),
    ('read', 'Read'),
    ('closed', 'Closed'),
)


class Contact(models.Model):
    subject = models.CharField(max_length=25, null=True)
    status = models.CharField(max_length=6, choices=STATUS, default='new')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Müşteri İletişim Bilgileri'
        verbose_name_plural = 'Müşteri İletişim Bilgileri'


class İnfo(models.Model):
    location = models.CharField(max_length=300, verbose_name="Adres")
    startedat = models.CharField(
        max_length=300, verbose_name="Kafe Açılış Saati")
    closedat = models.CharField(
        max_length=300, verbose_name="Kafe Kapanış Saati")
    email = models.CharField(max_length=300, verbose_name="Email Adresi")
    phone = models.CharField(max_length=300, verbose_name="Telefon Numarası")

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']
        verbose_name = 'Kafe İletişim Bilgileri'
        verbose_name_plural = 'Kafe İletişim Bilgileri'

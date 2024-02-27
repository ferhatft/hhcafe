from django.db import models
from django.conf import settings

# Create your models here.

    

class WinersModel(models.Model):
    name = models.CharField(max_length = 15,verbose_name = "İsim Ekleyin")
    image = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf Ekleyin")
    wintime = models.DateTimeField(verbose_name="Tarih Ekleyin",)
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Çekiliş Kazananları'
        verbose_name_plural = 'Çekiliş Kazananları'

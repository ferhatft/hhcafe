from django.db import models
from django.conf import settings

# Create your models here.

    

class PartnerModel(models.Model):
    # title = models.CharField(max_length = 50,verbose_name = "Ana Başlık Ekleyin" ,blank=True, null=True )
    # Subtitle = models.CharField(max_length = 100,verbose_name = "Alt Başlık Ekleyin" ,blank=True, null=True )
    name = models.CharField(max_length = 100,verbose_name = "İsim Ekleyin")
    image = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf Ekleyin")
    facebook = models.CharField(max_length = 3000,verbose_name = "Facebook Linki Ekleyin" ,blank=True, null=True )
    instagram = models.CharField(max_length = 3000,verbose_name = "İnstagram Linki Ekleyin",blank=True, null=True)
    alan = models.CharField(max_length = 50,verbose_name = "Çalışma Alanı Ekleyin",blank=True, null=True)
    
    contexttitle = models.CharField(max_length = 50,verbose_name = "Açıklama Başlık Ekleyin" ,blank=True, null=True )
    contextSubtitle = models.CharField(max_length = 300,verbose_name = "Açıklama Alt Başlık Ekleyin" ,blank=True, null=True )
    contextparagraf = models.CharField(max_length = 10000,verbose_name = "Açıklama Paragrafı  Ekleyin" ,blank=True, null=True )
    contextslogan = models.CharField(max_length = 100,verbose_name = "Açıklama Slogan Ekleyin" , null=True,blank=True )
    
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Partnerlerimiz'
        verbose_name_plural = 'Partnerlerimiz'

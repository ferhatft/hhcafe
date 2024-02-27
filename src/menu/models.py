from django.db import models

# Create your models here.

MENU_CHOICES = (
    ('kahveler','COFFEE BASED'),
    ('turkkahveleri', 'TÜRK KAHVESİ'),
    ('hotdrinks','HOT DRİNKS'),
    ('icedrinks','SOĞUK İÇECEKLER'),
    ('milhshake', 'MILK SHAKELER'),
    ('waffle','WAFFLE'),
)
    

class MenuModel(models.Model):
    title = models.CharField(max_length = 50,verbose_name = "Başlık Ekleyin")
    image = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf Ekleyin")
    aciklama = models.CharField(max_length =100,verbose_name = "Aççıklama Ekleyin")
    fiyat = models.CharField(max_length =10,verbose_name = "Fiyat Ekleyin",blank=True )
    bölüm = models.CharField(max_length=30, choices=MENU_CHOICES, default='kahveler')
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Menü'
        verbose_name_plural = 'Menü'



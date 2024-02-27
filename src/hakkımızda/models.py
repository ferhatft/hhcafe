from django.db import models

# Create your models here.

class AboutModel(models.Model):
    title = models.CharField(max_length = 300,verbose_name = "Başlık")
    image = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf Ekleyin")
    pragraf = models.CharField(max_length = 300,verbose_name = "pragraf")
    pragrafiki = models.CharField(max_length = 300,verbose_name = "pragrafiki")
    pragrafüç = models.CharField(max_length = 300,verbose_name = "pragrafüç")
    pragrafdört = models.CharField(max_length = 300,verbose_name = "pragrafdört")
    pragrafbeş = models.CharField(max_length = 300,verbose_name = "pragrafbeş" , blank=True)
    pragrafaltı = models.CharField(max_length = 300,verbose_name = "pragrafaltı", blank=True)
    pragrafyedi = models.CharField(max_length = 300, verbose_name = "pragrafyedi", blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Biz Kimiz'
        verbose_name_plural = 'Biz Kimiz'
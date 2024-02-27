from django.db import models

from ckeditor.fields import RichTextField

class TotalModel(models.Model):
    total = models.CharField(max_length = 50, verbose_name = "Toplam")
    def __str__(self):
        return self.total

    class Meta:
        ordering = ['total']
        verbose_name = 'Günlük satılan kahve Sayısı'
        verbose_name_plural = 'Günlük satılan Kahve Sayısı'



STATUS = (
    ('kazandı', 'Kazandı'),
    ('beklemede', 'Beklemede'),
)


class TotaltreeModel(models.Model):
    totalstudentcofee = models.CharField(null=True,max_length = 50, verbose_name = "Toplam kahve ( Öğrenci )")
    totaldoctorcofee = models.CharField(null=True,max_length = 50, verbose_name = "Toplam kahve ( Sağlık personeli ) ")
    
    def __str__(self):
        return 'Kahve Sayıları'

    class Meta:
        ordering = ['id']
        verbose_name = 'Yeşil Kutu Toplam Ağaçdaki  kahve Sayıları'
        verbose_name_plural = 'Yeşil Kutu Toplam Ağaçtaki Kahve Sayıları'



STATUS = (
    ('teslimedildi', 'Teslim Edildi'),
    ('beklemede', 'Beklemede'),
)


class PilregisterModel(models.Model):
    status = models.CharField(max_length=15, choices=STATUS, default='beklemede')
    name = models.CharField(max_length=30,verbose_name = "İsim-Soyisim",null=True)
    # email = models.EmailField(verbose_name = "Email adresi" ,null=True,blank=True)
    phone = models.CharField(max_length=11, verbose_name="Telefon Numarası",null=True)
    pill = models.CharField(max_length=50, verbose_name="Fiş Numarası")
    created_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.pill

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Kırmızı Kutu Fiş Kayıtı'
        verbose_name_plural = 'Kırmızı Kutu Fiş Kayıtları'



class Pillregistercontextmodel(models.Model):
    title = models.CharField(max_length=500,verbose_name = "Başlık Ekleyin", blank=True)
    subtitle = models.CharField(max_length=500,verbose_name = "Alt Başlık Ekleyin" , blank=True)
    pragraf            = RichTextField(verbose_name = "Açıklama Ekleyin" ,null=True, blank=True)
    slogan = models.CharField(max_length=500,verbose_name = "Slogan Ekleyin", blank=True)
    image = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf Ekleyin")


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Kırmızı Kutu Açıklaması '
        verbose_name_plural = 'Kırmızı Kutu Açıklaması'


class Kahvesayisimodel(models.Model):
    title = models.CharField(max_length=500,verbose_name = "Başlık Ekleyin", blank=True)
    subtitle = models.CharField(max_length=500,verbose_name = "Alt Başlık Ekleyin" , blank=True)
    pragraf            = RichTextField(verbose_name = "Açıklama Ekleyin" ,null=True, blank=True)
    slogan = models.CharField(max_length=500,verbose_name = "Slogan Ekleyin", blank=True)
    image = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf Ekleyin")


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Şeffaf Kutu Açıklaması '
        verbose_name_plural = 'Şeffaf Kutu Açıklaması'




class Yardımsayisimodel(models.Model):
    title = models.CharField(max_length=500,verbose_name = "Başlık Ekleyin", blank=True)
    subtitle = models.CharField(max_length=500,verbose_name = "Alt Başlık Ekleyin", blank=True )
    pragraf            = RichTextField(verbose_name = "Açıklama Ekleyin" ,null=True, blank=True)
    slogan = models.CharField(max_length=500,verbose_name = "Slogan Ekleyin", blank=True)
    image = models.FileField(blank=True ,null=True, verbose_name="Fotoğraf Ekleyin")


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Turuncu kutu Açıklaması'
        verbose_name_plural = 'Turuncu kutu Açıklaması'
        


class Kahveagacimodel(models.Model):
    titlestudent = models.CharField(max_length=500,verbose_name = "Öğrenci Ağacı Başlığı", blank=True,null=True)
    subtitlestudent = models.CharField(max_length=500,verbose_name = "Öğrenci ağacı Alt Başlık " , blank=True,null=True)
    pragrafstudent           = RichTextField(verbose_name = "Öğrenci ağacı Açıklama" ,null=True, blank=True)
    sloganstudent = models.CharField(max_length=500,verbose_name = "Öğrenci ağacı Slogan ", blank=True,null=True)
    imagetudent = models.FileField(blank=True ,null=True, verbose_name="Öğrenci Fotoğraf Ekleyin")

    titledoctor = models.CharField(max_length=500,verbose_name = "Sağlık Çalışanı Ağacı Başlık ", blank=True,null=True)
    subtitledoctor = models.CharField(max_length=500,verbose_name = "Sağlık Çalışanı Ağacı Alt Başlık " , blank=True,null=True)
    pragrafdoctor            = RichTextField(verbose_name = "Sağlık Çalışanı Ağacı Açıklama " ,null=True, blank=True)
    slogandoctor = models.CharField(max_length=500,verbose_name = "Sağlık Çalışanı Ağacı Slogan ", blank=True,null=True)
    imagedoctor = models.FileField(blank=True ,null=True, verbose_name="Sağlık Çalışanı Ağacı Fotoğraf ")



    # aynı şekilde öğrenci ve doktor için ekle buradan tek bir odelde olsun 

    def __str__(self):
        return 'Kahve ağacı açıklaması'

    class Meta:
        ordering = ['id']
        verbose_name = 'Yeşil kutu Açıklamaları'
        verbose_name_plural = 'Yeşil kutu Açıklamaları'





class kahvestudentyardimModel(models.Model):
    name = models.CharField(max_length=30,verbose_name = "İsim-Soyisim",null=True)
    # email = models.EmailField(verbose_name = "Email adresi" ,null=True,blank=True)
    phone = models.CharField(max_length=11, verbose_name="Telefon Numarası",null=True,)
    note  = models.TextField(verbose_name = "Not Ekleyin" ,null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Yeşil Kutu Eklenen kahve ( Öğrenci )'
        verbose_name_plural = 'Yeşil Kutu Eklenen kahveler ( Öğrenci )'



class kahvedoctoryardimModel(models.Model):   
    name = models.CharField(max_length=30,verbose_name ="İsim-Soyisim", null=True)
    # email = models.EmailField(verbose_name = "Email adresi" ,null=True,blank=True)
    phone = models.CharField(max_length=11, verbose_name="Telefon Numarası",null=True,)
    note  =models.TextField(verbose_name = "Not Ekleyin" ,null=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Yeşil Kutu Eklenen kahve (doktor)'
        verbose_name_plural = 'Yeşil Kutu Eklenen kahveler (doktor)'








class Orangeboxmodel(models.Model):
    first = models.CharField(max_length=15,verbose_name = "Birinci Satırı Ekleyin" , blank=True)
    second = models.CharField(max_length=15,verbose_name = "İkinci Satırı Ekleyin" , blank=True)
    third = models.CharField(max_length=15,verbose_name = "Üçüncü Satırı Ekleyin", blank=True)


    def __str__(self):
        return self.first

    class Meta:
        ordering = ['first']
        verbose_name = 'Turuncu kutu üzrindeki yazılar'
        verbose_name_plural = 'Turuncu kutu üzrindeki yazılar'



class Redboxmodel(models.Model):
    first = models.CharField(max_length=15,verbose_name = "Birinci Satırı Ekleyin" , blank=True)
    second = models.CharField(max_length=15,verbose_name = "İkinci Satırı Ekleyin" , blank=True)
    third = models.CharField(max_length=15,verbose_name = "Üçüncü Satırı Ekleyin", blank=True)


    def __str__(self):
        return self.first

    class Meta:
        ordering = ['first']
        verbose_name = 'Kırmızı kutu üzrindeki yazılar'
        verbose_name_plural = 'Kırmızı kutu üzrindeki yazılar'




class Greeenboxmodel(models.Model):
    first = models.CharField(max_length=15,verbose_name = "Birinci Satırı Ekleyin" , blank=True)
    second = models.CharField(max_length=15,verbose_name = "İkinci Satırı Ekleyin" , blank=True)


    def __str__(self):
        return self.first

    class Meta:
        ordering = ['first']
        verbose_name = 'Yeşil kutu üzrindeki yazılar'
        verbose_name_plural = 'Yeşil kutu üzrindeki yazılar'













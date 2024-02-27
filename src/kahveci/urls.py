from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexview, name="index"),
    # path('çekilişe_katıl/', views.cekilisview, name="cekilis"),
    path('about/', views.aboutview, name="about"),
    path('menu/', views.menuview, name="menu"),
    path('iletisim/', views.contacview, name="contact"),
    # path('kazananlar/', views.kazananview, name="kazananlar"),
    path('partnerlerimiz/', views.partnerview, name="partner"),
    path('kahveal/', views.kahvealview, name="kahveal"),
    
    path('kahve_agaci_fis_kayitlari/', views.pilregisterview, name="fiskayıt"),


    # path('gizlilik-politikası/', views.gizlilikpolitikasiView , name="gpolitikasi"),
    # path('kullanıcı-sözleşmesi/', views.kullanimşartlariView , name="ksözleşmesi"),
    # path('hakkimda/', views.aboutView, name="about"),
    # path('emlak-bilgisi-al/', include("contact.urls")),
    # path('sikca-sorulan-sorular/', include("sorular.urls")),
    # path('blog/', include("makale.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

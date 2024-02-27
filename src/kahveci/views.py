from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from partial_date import PartialDate

from anasayfa.models import (
                            TotalModel, 
                            Kahvesayisimodel, 
                            Yardımsayisimodel,
                            Kahveagacimodel,
                            Orangeboxmodel,
                            Redboxmodel,
                            Greeenboxmodel,
                            TotaltreeModel,
                            Pillregistercontextmodel,
)
from anasayfa.forms import pillregisterForm,kahvestudentyardimForm,kahvedoctoryardimForm

from hakkımızda.models import AboutModel
from menu.models import MenuModel
from iletisim.models import Contact, İnfo
from iletisim.forms import ContactForm

#from kazananlar.models import WinersModel
from partnerlerimiz.models import PartnerModel


def indexview(request):
    pillregistercontextmodel = Pillregistercontextmodel.objects.last()
    kahvesayisimodel = Kahvesayisimodel.objects.last()
    yardımsayisimodel = Yardımsayisimodel.objects.last()
    kahveagacimodel = Kahveagacimodel.objects.last()
    totalModel = TotalModel.objects.all()
    totaltreemodel =TotaltreeModel.objects.last()
    orangeboxmodel = Orangeboxmodel.objects.last()
    redboxmodel = Redboxmodel.objects.last()
    greeenboxmodel = Greeenboxmodel.objects.last()
    obj = totalModel.last()

    formiki = kahvestudentyardimForm(request.POST)
    
    formpill = pillregisterForm(request.POST)

    if request.method == 'POST':
        form = kahvedoctoryardimForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            form.save()
            # messages.success(
            # request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapılcaktır...')
            return redirect('http://ferhattugrul.online/')
    else:
        form = kahvedoctoryardimForm()

    context = {
        'obj': obj,
        'form': form,
        'formiki':formiki,
        'formpill':formpill,
        'kahvesayisimodel': kahvesayisimodel,
        'yardımsayisimodel': yardımsayisimodel,
        'kahveagacimodel': kahveagacimodel,
        'orangeboxmodel':orangeboxmodel,
        'redboxmodel':redboxmodel,
        'greeenboxmodel':greeenboxmodel,
        'totaltreemodel':totaltreemodel,
        'pillregistercontextmodel':pillregistercontextmodel,
        
    }

    return render(request, "index.html", context)



def kahvealview(request):
    obj = İnfo.objects.last()
    if request.method == 'POST':
        form = kahvestudentyardimForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']

            form.save()
            # messages.success(
            # request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapılcaktır...')
            return redirect('http://ferhattugrul.online/')
    else:
        form = kahvestudentyardimForm()

    # context = {
    #     'form': form,
    #     'obj':obj,
    # }
    # return render(request, "kahveal.html", context)
    
    
    # herhngi bi yere return yapmamıza gerek yok action ile sadece formu kullanıyoruz herhangi bir template de kullanmayacağız bi view i 


def pilregisterview(request):
    # obj = İnfo.objects.last()
    if request.method == 'POST':
        form = pillregisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            pill = form.cleaned_data['pill']

            form.save()
            # messages.success(
            # request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapılcaktır...')
            return redirect('index')
    else:
        form = pillregisterForm()

    # context = {
    #     'form': form,
    #     # 'obj':obj,
    # }
    # return render(request, "index.html", context)



def aboutview(request):
    aboutModel = AboutModel.objects.last()
    return render(request, "about.html", {"aboutModel": aboutModel})


def menuview(request):
    kahveler = MenuModel.objects.filter(bölüm="kahveler")
    turkkahveleri = MenuModel.objects.filter(bölüm="turkkahveleri")
    hotdrinks = MenuModel.objects.filter(bölüm="hotdrinks")
    icedrinks = MenuModel.objects.filter(bölüm="icedrinks")
    milhshake = MenuModel.objects.filter(bölüm="milhshake")
    waffle = MenuModel.objects.filter(bölüm="waffle")


    # print("-----------------------------------------------------------------")
    # obj = çaylar.last()

    # print(obj.aciklama)
    # # print(dir(çaylar))

    # print("-----------------------------------------------------------------")
    # print(sıcakçikolata)
    # obj2 = sıcakçikolata.first()
    # print(obj2.aciklama)

    # # print(dir(sıcakçikolata))

    print("-----------------------------------------------------------------")
    context = {
        "turkkahveleri": turkkahveleri,
        "kahveler": kahveler,
        "hotdrinks": hotdrinks,
        "icedrinks": icedrinks,
        "milhshake": milhshake,
        "waffle": waffle,
    }

    return render(request, "menu.html", context)


# def infoview(request):
#     obj = İnfo.objects.all()

#     print("-----------------------------------------------------------------")
#     print(obj)


#     print("-----------------------------------------------------------------")
#     context = {

#     }

#     return render(request, "contac.html", context)


def contacview(request):
    obj = İnfo.objects.last()

    # print("-----------------------------------------------------------------")
    # # first = obj.first()
    # print(obj)
    # print(dir(obj))
    # # print(first)
    # # print(first.location)

    # print("-----------------------------------------------------------------")

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = form.cleaned_data['subject']
            # phone = form.cleaned_data['phone']

            form.save()
            # messages.success(
            # request, 'Mesajınız başarıyla gönderildi. En kısa sürede size dönüş yapılcaktır...')
            return redirect('index')
    else:
        form = ContactForm()

    context = {
        'obj': obj,
        'form': form
    }
    return render(request, "contac.html", context)


def kazananview(request):
    obj = WinersModel.objects.all()
   
    context = {
        'obj': obj,
    }
    return render(request, "kazanan.html", context)


def partnerview(request):
    objects = PartnerModel.objects.all()

    context = {
        'objects': objects
    }
    return render(request, "partners.html", context)

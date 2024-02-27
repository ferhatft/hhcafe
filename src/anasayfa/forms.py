from django import forms
from .models import PilregisterModel, kahvedoctoryardimModel, kahvestudentyardimModel


class pillregisterForm(forms.ModelForm):
    class Meta:
        model = PilregisterModel
        fields = ['name', 'phone', 'pill']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsim-Soyisim'}),
            # 'email': forms.TextInput(attrs={'placeholder': 'E-mail Adresiniz'}),
            'phone':
            forms.TextInput(attrs={'placeholder': 'Telefon Numaranız'}),
            'pill': forms.TextInput(attrs={'placeholder': 'Fiş Numaranız'}),
        }

    def __init__(self, *args, **kwargs):
        super(pillregisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class kahvedoctoryardimForm(forms.ModelForm):
    class Meta:
        model = kahvedoctoryardimModel
        fields = ['name', 'phone', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsim-Soyisim'}),
            # 'email': forms.TextInput(attrs={'placeholder': 'E-mail Adresiniz'}),
            'phone':forms.TextInput(attrs={'placeholder': 'Telefon Numaranız'}),
            'note': forms.Textarea(attrs={'placeholder': 'Notunuz'}),
        }

    def __init__(self, *args, **kwargs):
        super(kahvedoctoryardimForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class kahvestudentyardimForm(forms.ModelForm):
    class Meta:
        model = kahvestudentyardimModel
        fields = ['name', 'phone', 'note']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'İsim-Soyisim'}),
            # 'email': forms.TextInput(attrs={'placeholder': 'E-mail Adresiniz'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon Numaranız'}),
            'note': forms.Textarea(attrs={'placeholder': 'Notunuz'}),
        }

    def __init__(self, *args, **kwargs):
        super(kahvestudentyardimForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

from django import forms
from django.forms import Select

from .models import Distributer, Retailer, AdolfAdmin

class UserCreation(forms.Form):
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'type': 'tel'}))
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    password = forms.CharField(widget=forms.PasswordInput)

class UserRole(forms.Form):
    CHOICES = (
        ('1', 'Adolf Admin'),
        ('2', 'Distributer'),
        ('3', 'Retailer'),
    )

    choices = forms.ChoiceField(choices=CHOICES, widget=Select(attrs={'onchange': 'showForm();'}), initial=CHOICES[1])

    class Media:
        js = (
            'dashboard/js/showform.js'
        )

class NewAdmin(forms.ModelForm):
    class Meta:
        model = AdolfAdmin
        exclude = ['user', 'photo']

class NewDist(forms.ModelForm):
    class Meta:
        model = Distributer
        fields = ['adolfAdmin', 'company_name_dist', 'company_address_dist']
        labels = {'adolfAdmin': 'Adolf Admin', 'company_name_dist': 'Company Name', 'company_address_dist': 'Company Address'}

class NewRet(forms.ModelForm):
    class Meta:
        model = Retailer
        fields = ['distributer', 'company_name_ret', 'company_address_ret']
        labels = {'company_name_ret': 'Shop Name', 'company_address_ret': 'Shop Address'}

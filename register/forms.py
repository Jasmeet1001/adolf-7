from django import forms

class LoginForm(forms.Form):
    phone_number = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'type': 'tel', 'class' : 'form-control id_phNum', 'required':'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control id_phNum', 'required':'required'}))
    

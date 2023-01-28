from django import forms
from .models import User

class login_form(forms.ModelForm):
    password1 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['phone_number', 'password1']
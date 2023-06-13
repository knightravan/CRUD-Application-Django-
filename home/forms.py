from django import forms
from .models import regi
from django.core import validators

class detregi(forms.ModelForm):
	class Meta:
		model=regi
		fields=['name','email','password']
		widgets={
		'name': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.TextInput(attrs={'class':'form-control'}),
		'password': forms.PasswordInput(attrs={'class':'form-control'}),
		}
#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User 
from django.contrib import auth
from datetime import datetime
from .models import *

ANIO_ACTUAL = datetime.now().year
ANIO_FIN    = ANIO_ACTUAL - 99
MES_NACIMIENTO_CHOICES = (
			('1','ENERO'),('2','FEBRERO'),('3','MARZO'),('4','ABRIL'),
			('5','MAYO'),('6','JUNIO'),('7','JULIO'),('8','AGOSTO'),
			('9','SEPTIEMBRE'),('10','OCTUBRE'),('11','NOVIEMBRE'),('12','DICIEMBRE'),
		)
class RegistroForm(forms.Form):
	
	
	email				= forms.EmailField(widget=forms.EmailInput(attrs=dict({'class':'required','placeholder':'Correo electronico','required':'required'})),required=True)
	password			= forms.CharField(widget=forms.PasswordInput(attrs=dict({'placeholder':'Contraseña'})),required=True)
	nombre 				= forms.CharField(widget=forms.TextInput(attrs=dict({'placeholder':'Nombre','required':'required'})),required=False)
	apellido			= forms.CharField(widget=forms.TextInput(attrs=dict({'placeholder':'Apellido'})),required=False)
	mes_nacimiento 		= forms.ChoiceField(choices=MES_NACIMIENTO_CHOICES,required=False)
	dia_nacimiento 		= forms.ChoiceField(choices=((str(x), x) for x in range(1,32)),required=False)
	anio_nacimiento     = forms.ChoiceField(choices=((str(x), x) for x in range(ANIO_ACTUAL,ANIO_FIN,-1)),required=False)

	def clean_email(self):
		email = self.cleaned_data["email"]
		try:
			User._default_manager.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('email duplicado')

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		exclude = ['last_login','is_superuser','is_staff','is_active','date_joined','groups','user_permissions','password','username',]



class ProfileForm(forms.ModelForm):

	mes_nac 		= forms.ChoiceField(choices=MES_NACIMIENTO_CHOICES,required=False)
	dia_nac 		= forms.ChoiceField(choices=((str(x), x) for x in range(1,32)),required=False)
	anio_nac     = forms.ChoiceField(choices=((str(x), x) for x in range(ANIO_ACTUAL,ANIO_FIN,-1)),required=False)
	avatar 		= forms.ImageField()

	class Meta:
		model = UserProfile
		exclude = ['user','activation_key','key_expires']
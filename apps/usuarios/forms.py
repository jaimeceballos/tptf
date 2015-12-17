#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User 
from django.contrib import auth
from datetime import datetime

ANIO_ACTUAL = datetime.now().year
ANIO_FIN    = ANIO_ACTUAL - 99

class RegistroForm(forms.Form):
	MES_NACIMIENTO_CHOICES = (
			('1','ENERO'),('2','FEBRERO'),('3','MARZO'),('4','ABRIL'),
			('5','MAYO'),('6','JUNIO'),('7','JULIO'),('8','AGOSTO'),
			('9','SEPTIEMBRE'),('10','OCTUBRE'),('11','NOVIEMBRE'),('12','DICIEMBRE'),
		)
	
	email				= forms.EmailField(widget=forms.EmailInput(attrs=dict({'placeholder':'Correo electronico'})),required=True)
	password			= forms.CharField(widget=forms.PasswordInput(attrs=dict({'placeholder':'Contraseña'})),required=True)
	nombre 				= forms.CharField(widget=forms.TextInput(attrs=dict({'placeholder':'Nombre'})),required=False)
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
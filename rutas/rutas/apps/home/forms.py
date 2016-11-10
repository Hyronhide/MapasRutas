from django.contrib.auth.models import User
from django import forms
from rutas.apps.home.models import *

#-----------------------------------------Modulo Lugares---------------------------------------------

class add_tipo_lugar_form (forms.ModelForm):
	class Meta:
		model = TipoLugar
		fields = '__all__'

class add_lugar_form(forms.ModelForm):
	class Meta:
		model 	= Lugar
		fields = '__all__'

#-------------------------------------------Modulo Usuarios--------------------------------------------

class Login_form(forms.Form):
	usuario = forms.CharField(widget = forms.TextInput())	
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))	
	fields = '__all__'

class UserForm(forms.ModelForm):
	password = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	class Meta:
		model = User
		fields = ['username','email',]		

class contact_form(forms.Form):
	correo 	= forms.EmailField(widget = forms.TextInput())
	titulo 	= forms.CharField(widget = forms.TextInput())
	comentario 	= forms.CharField(widget = forms.Textarea())
	#fields = '__all__'

#-------------------------------------Modulo Empresas--------------------------------------------------		

class add_empresa_form(forms.ModelForm):
	class Meta:
		model = Empresa
		fields = '__all__'

#---------------------------------------Modulo Rutas---------------------------------------------------

class agregar_ruta_form(forms.ModelForm):
	class Meta:
		model 	= Ruta
		fields = '__all__'

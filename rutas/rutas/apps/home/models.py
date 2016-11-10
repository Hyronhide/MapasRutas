from django.db import models
from django.contrib.auth.models import User

class user_profile(models.Model):
	

	user 		= models.OneToOneField(User)	
	#photo 		= models.ImageField(upload_to=url)
	telefono 	= models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username

TIPO_BUS = (
	('buseton','buseton'),
	('buseta','buseta'),
	)

class Empresa(models.Model):

	nombre		= models.CharField(max_length = 45)
	logo		= models.ImageField(upload_to='empresa', default='empresa/empresa.png', blank=True)
	#logo		= models.ImageField(upload_to = url, null = True, blank = True)	
	nit    		= models.DecimalField(max_digits = 11, decimal_places = 0)
	telefono 	= models.CharField(max_length = 45)
	#Representante_de_la_empresa= models.CharField(max_length = 45)
	
	def __unicode__ (self):
		return self.nombre

class TipoLugar(models.Model):
	nombre		= models.CharField(max_length = 45, unique=True)
	
	def __unicode__ (self):
		return self.nombre

class Lugar(models.Model):	
	
	nombre		= models.CharField(max_length = 250, unique=True)
	latitud		= models.IntegerField( unique=True)
	longitud	= models.IntegerField( unique=True)
	tipo 		= models.ForeignKey(TipoLugar)
	imagen		= models.ImageField(upload_to='empresa', default='empresa/empresa.png', blank=True)
	#imagen		= models.ImageField(upload_to = url, null = True, blank = True)
	primario  	= models.BooleanField(default=False)

	def __unicode__ (self):
		return self.nombre

class Ruta(models.Model):	

	numero 			= models.CharField(max_length = 45)
	recorrido		= models.CharField(max_length = 45)
	tipo 			= models.CharField(max_length = 45, choices = TIPO_BUS)
	foto			= models.ImageField(upload_to='empresa', default='empresa/empresa.png', blank=True)
	lugares			= models.ManyToManyField(Lugar, blank = True)
	empresas		= models.ForeignKey(Empresa)

	def __unicode__ (self):
		return self.numeroRuta + self.recorrido + self.fotoRuta


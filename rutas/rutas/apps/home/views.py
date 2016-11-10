from django.shortcuts import render_to_response,render
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User ##
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.db.models import Q

from rutas.apps.home.forms import *
from rutas.apps.home.models import *
from django.contrib import messages

#---------------------------------Modulo Lugares----------------------------------------------------------

#def index_view (request):
#   return render_to_response('home/Lugares/index.html', context_instance = RequestContext(request))

def add_tipo_lugar_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_tipo_lugar_form (request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() #guarda la informacion           
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/')
	else:
		formulario = add_tipo_lugar_form () 
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('home/Lugares/agregar_tipo_lugar.html', ctx,context_instance = RequestContext(request))   

def add_lugar_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_lugar_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() #guarda la informacion
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/')
	else:
		formulario = add_lugar_form()   
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('home/Lugares/Agregar_Lugar.html', ctx,context_instance = RequestContext(request))

def lugares_view(request, pagina):
	lista_lug = Lugar.objects.all()
	paginator = Paginator(lista_lug, 5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		lugares = paginator.page(page)
	except (EmptyPage,InvalidPage):
		lugares = paginator.page(paginator.num_pages)

	ctx = {'lugares':lugares}   
	return render_to_response ('home/Lugares/lugares.html', ctx, context_instance = RequestContext(request))

def ver_view(request, id_lug):
	lug = Lugar.objects.get(id = id_lug)    
	ctx = {'lugar':lug}
	return render_to_response('home/Lugares/ver.html', ctx, context_instance = RequestContext(request))


def edit_lugar_view(request, id_lug):
	info = ""
	lug = Lugar.objects.get(pk = id_lug)
	if request.method == "POST":
		formulario = add_lugar_form(request.POST, request.FILES, instance = lug)
		if formulario.is_valid():
			edit_lug = formulario.save(commit = False)
			formulario.save_m2m()
			edit_lug.status = True
			edit_lug.save()
			info = "Guardado Satisfactoriamente"
			messages.success(request, '<a href="/ruta/page/1">Guardado Satisfactoriamente</a>', extra_tags='html_safe')
			#return HttpResponseRedirect ('/')
			return HttpResponseRedirect ('/lugares/page/1')
	else:
		formulario = add_lugar_form(instance = lug)
	ctx = {'form':formulario, 'informacion':info}   
	return render_to_response('home/Lugares/edit_lugar.html',ctx,context_instance = RequestContext(request))

def del_lugar_view(request, id_lug):
	info = "inicializando"
	try:
		lugar = Lugar.objects.get(pk = id_lug)
		lugar.delete()
		info = "lugar Eliminado Correctamente"
		return HttpResponseRedirect('/lugares/page/1')
	except:
		info = "no se puede eliminar el lugar"
		return render_to_response('home/Lugares/lugares.html',ctx,context_instance = RequestContext(request))
		#return HttpResponseRedirect('/Lugares/')

#----------------------------------Modulo Usuarios--------------------------------------------------------

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():#verificacmos si el usuario ya esta authenticado o logueado
		return HttpResponseRedirect('/')#si esta logueado lo redirigimos a la pagina principal
	else: #si no esta authenticado 
		if request.method == "POST":
			formulario = Login_form(request.POST) #creamos un objeto de Loguin_form
			if formulario.is_valid(): #si la informacion enviada es correcta        
				usu= formulario.cleaned_data['usuario'] #guarda informacion ingresada del formulario
				pas= formulario.cleaned_data['clave'] #guarda informacion ingresada del formulario
				usuario = authenticate(username = usu,password = pas)#asigna la autenticacion del usuario
				if usuario is not None and usuario.is_active:#si el usuario no es nulo y esta activo
					login(request,usuario)#se loguea al sistema con la informacion de usuario
					return HttpResponseRedirect('/')#redirigimos a la pagina principal
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form() #creamos un formulario nuevo limpio
		ctx = {'form':formulario, 'mensaje':mensaje}#variable de contexto para pasar info a login.html
		return render_to_response('home/login.html',ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request)# funcion de django importda anteriormente
	return HttpResponseRedirect('/')# redirigimos a la pagina principal

def user_view(request): 
	us = User.objects.get(username= request.user.username)
	ctx={'user':us}
	return render_to_response('home/user.html',ctx,context_instance = RequestContext(request))  

def edit_user_view(request):
	info = ""   
	us = User.objects.get(id = request.user.id)
	if request.method == "POST":
		formulario = UserForm(request.POST, request.FILES, instance = us)       
		if formulario.is_valid():
			clave = formulario.cleaned_data['password']
			formulario.password = us.set_password(clave)
			edit_user = formulario.save(commit = False)
			formulario.save_m2m()
			edit_user.status = True
			edit_user.save()
			info = "Guardado Satisfactoriamente"
			#return HttpResponseRedirect ('/')
			return HttpResponseRedirect ('/user/')
	else:
		formulario = UserForm(instance = us)
	ctx = {'form':formulario, 'informacion':info}   
	return render_to_response('home/edit_user.html',ctx,context_instance = RequestContext(request))             
	
def gracias_view (request):
	html = '<html><body>"Gracias por enviarnos su comentario...</body></html>'
	return HttpResponse(html)   

def contacto_view (request):
		info_enviado = False 
		email = ""
		name  = ""
		text = ""
		title = ""
		if request.method == "POST":
			formulario = contact_form(request.POST)
			if formulario.is_valid():
				info_enviado = True
				email   = formulario.cleaned_data['correo']
				title   = formulario.cleaned_data['titulo']
				text    = formulario.cleaned_data['comentario']

				'''Bloque configuracion de envio por GMAIL'''
				to_admin = 'contactoelbu@gmail.com'
				html_content = "informacion recibida de %s <br> ---Mensaje--- <br> %s"%(email,text)
				msg = EmailMultiAlternatives('correo de contacto', html_content, 'from@gmail.com',[to_admin])
				msg.send()
				'''Fin del bloque'''
		else:
			formulario = contact_form()     
		ctx = {'form':formulario, 'email':email, 'title':title, 'text':text, 'info_enviado':info_enviado}   
		return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))

#-----------------------------------Modulo Empresas-------------------------------------------------------

def index_view(request):
	query = request.GET.get('q','')
	query2 = request.GET.get('x','')
	if query and query2:
		qset = (
			Q(lugares__nombre__icontains=query)and
			Q(lugares__nombre__icontains=query2)
		)
		results = Ruta.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("home/empresa/index.html", {
		"results": results,
		"query": query,
		"query2": query2
	},context_instance=RequestContext(request))     
	
	
def add_empresa_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_empresa_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save() #Guarda la informacion
			info = "Guardado Satisfactoriamente"
			return render_to_response('home/empresa/thanks_empresa.html',context_instance=RequestContext(request))
			#return HttpResponseRedirect ('/producto/%s' %add.id)
	else:
		formulario = add_empresa_form()
	ctx = {'form' :formulario,'informacion':info}
	return render_to_response('home/empresa/add_empresa.html',ctx,context_instance = RequestContext(request))

def empresa_view (request):
	lista_empre = Empresa.objects.all()

	paginator = Paginator(lista_empre, 5)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		empresa = paginator.page(page)
	except (EmptyPage,InvalidPage):
		empresa = paginator.page(paginator.num_pages)
		
	ctx = {'empresa':empresa}
	return render_to_response('home/empresa/empresa.html', ctx, context_instance = RequestContext(request))

def single_empresa_view(request, id_empresa):
	empresa = Empresa.objects.get(id = id_empresa)
	ctx = {'empresa': empresa}
	return render_to_response('home/empresa/single_empresa.html', ctx,context_instance = RequestContext(request))

def eliminar_empresa_view(request, id_empresa):
	info = "inicializando"
	try:
		prod = Empresa.objects.get(pk = id_empresa)
		prod.delete()
		info = "Empresa Eliminada Correctamente"
		return render_to_response('home/empresa/eliminar_empresa.html',context_instance=RequestContext(request))
	except:
		info = "Empresa no se puede eliminar"
		#return render_to_response('home/productos.html', context_instance = RequestContext(request))
		return render_to_response('home/empresa/index.html', ctx,context_instance = RequestContext(request))

def edit_empresa_view(request, id_empresa):
	info = ""
	empresa = Empresa.objects.get(pk = id_empresa)
	if request.method == "POST":
		formulario = add_empresa_form(request.POST, request.FILES, instance= empresa)
		if formulario.is_valid():
			edit_empresa = formulario.save(commit = False)
			formulario.save_m2m()
			edit_empresa.status = True
			edit_empresa.save()
			info = "Guardado Satisfactoriamente"
			return render_to_response('home/empresa/thanks_editar.html',context_instance = RequestContext(request))
	else:
		formulario = add_empresa_form(instance = empresa)       
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('home/empresa/edit_empresa.html',ctx,context_instance = RequestContext(request))  

#--------------------------------------Modulo Rutas-------------------------------------------------------- 

def agregar_rutas_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = agregar_ruta_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() #guarda la informacion
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/')
	else:
		formulario = agregar_ruta_form()    

	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('home/Rutas/add_rutas.html', ctx,context_instance = RequestContext(request))

def del_rutas_view(request, id_rut):
	info = "inicializando"
	try: 
		rut = Ruta.objects.get(pk = id_rut)
		rut.delete()
		info = "Ruta Eliminada Correctamente"
		return HttpResponseRedirect('/ruta/page/1')
	except: 
		info = "La Ruta No Se Puede Eliminar"
	return render_to_response('home/Rutas/add_rutas.html', ctx,context_instance = RequestContext(request))

def edit_ruta_view(request, id_rut):
	info = ""
	rut = Ruta.objects.get(pk = id_rut)
	if request.method == "POST":
		formulario = agregar_ruta_form(request.POST,request.FILES, instance = rut)
		if formulario.is_valid():
			edit_rut=formulario.save(commit = False)
			formulario.save_m2m()
			edit_rut.status = True
			edit_rut.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/ruta/page/1')     
		else:
			formulario = agregar_ruta_form(instance = rut)
			ctx = {'form':formulario,'informacion':info}
	return render_to_response('home/Rutas/edit_rutas.html', ctx, context_instance =RequestContext(request))

############################## AQUI PROFE MIRE ###################################
def single_ruta_view(request, id_rut):
	rut = Ruta.objects.get(id = id_rut)
	lugares = rut.lugares.all()
	longitud = []
	latitud = []
	cont = 0
	for a in lugares:	
		
		longitud.append("-76.561826")
		latitud.append("2.4831121")
		cont = cont + 1


	   
	print(longitud) 
	print(latitud)  
	print(cont)
	ctx = {'rutas':rut,'latitud':latitud,'longitud':longitud,'lugares':lugares,'cont':cont}
	return render_to_response('home/Rutas/single_ruta.html', ctx, context_instance = RequestContext(request))   
##################################################################################
def ruta_view (request, pagina):
	lista_rutas = Ruta.objects.all() 
	paginator =Paginator(lista_rutas, 5)
	try:
		page = int(pagina) 
	except: 
		page = 1
	try:
		rutas = paginator.page(page)
	except (EmptyPage,InvalidPage):
		rutas = paginator.page(paginator.num_pages)
		
	ctx = {'rutas':rutas}    
	return render_to_response('home/Rutas/rutas.html',ctx, context_instance = RequestContext(request))  

#------------------------------------------BUSCAR RUTAS----------------------------------------------------

def buscar_view(request):
	query = request.GET.get('q','')
	query2 = request.GET.get('x','')
	if query and query2:
		qset = (
			Q(lugares__nombre__icontains=query)and
			Q(lugares__nombre__icontains=query2)
		)
		results = Ruta.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response("home/buscarRuta.html", {
		"results": results,
		"query": query,
		"query2": query2
	},context_instance=RequestContext(request))     


def single_ruta_ver_view(request):

	return render(request,"home/Rutas/polilinea.html",locals())
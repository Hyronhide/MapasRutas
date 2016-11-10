from django.conf.urls import patterns, url 
from .views import *
urlpatterns = [

#-------------------------- Modulo Lugares---------------------------------------------------

	#url(r'^$',index_view, name = 'vista_principal'),
	url(r'^add/tipo_lugar/$',add_tipo_lugar_view, name = 'vista_agregar_tipo_lugar'),
	url(r'^add/lugar/$',add_lugar_view, name = 'vista_agregar_lugar'),
	url(r'^lugares/$', lugares_view, name = 'vista_lugares'),
	url(r'^lugar/(?P<id_lug>.*)/$', ver_view, name = 'vista_ver'),
	url(r'^lugares/page/(?P<pagina>.*)/$', lugares_view, name = 'vista_lugares'),	
	url(r'^edit/lugar/(?P<id_lug>.*)/$',edit_lugar_view, name = 'vista_editar_lugar'),	
	url(r'^del/lugar/(?P<id_lug>.*)/$',del_lugar_view, name = 'vista_eliminar_lugar'),

#---------------------------Modulo Usuarios--------------------------------------------------

	url(r'^login/$',login_view , name = 'vista_login'),
	url(r'^logout/$',logout_view, name = 'vista_logout'),
	url(r'^edit_user/$',edit_user_view, name = 'vista_edit_user'),
	url(r'^user/$',user_view, name = 'vista_user'),	
	url(r'^contacto/$', contacto_view, name = 'vista_contacto'),	
	url(r'^gracias/',gracias_view,name = 'vista_gracias'),

#----------------------------Modulo Empresas--------------------------------------------------

	url(r'^$',index_view,name ='vista_principal'),
	url(r'^add/empresa/$',add_empresa_view,name ='vista_add_empresa'),
	url(r'^empresa/$',empresa_view, name ='vista_empresa'),
	url(r'^empresa/page/(?P<pagina>.*)/$', empresa_view, name = 'vista_empresa'),
	url(r'^empresa/(?P<id_empresa>.*)/$', single_empresa_view, name = 'vista_single_empresa'),
	url(r'^eliminar/empresa(?P<id_empresa>.*)/$', eliminar_empresa_view, name = 'vista_empresa'),
	url(r'^edit/empresa/(?P<id_empresa>.*)/$', edit_empresa_view, name = 'vista_editar_empresa'),

#----------------------------Modulo Rutas-------------------------------------------------------

	url(r'^add/rutas/$',agregar_rutas_view, name = 'vista_agregar_rutas'),
	#url(r'^del/rutas/(?P<id_rut>.*)/$',' del_rutas_view', name = 'vista_eliminar_ruta'),
	url(r'^edit/rutas/(?P<id_rut>.*)/$',edit_ruta_view, name = 'vista_editar_ruta'),
	url (r'^ruta/page/(?P<pagina>.*)/$',ruta_view, name = 'vista_ruta'),
	url (r'^ruta/(?P<id_rut>.*)/$',single_ruta_view, name = 'vista_single_ruta'),
	url (r'^ruta_ver/$',single_ruta_ver_view, name = 'vista_single_ruta_ver'),

#----------------------------BUSCAR RUTA--------------------------------------------------------

	url (r'^buscar/$',buscar_view,name='vista_buscar'),
]
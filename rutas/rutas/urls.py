from django.conf.urls import patterns, include, url
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete   
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^',include('rutas.apps.home.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    # url(r'^$', 'add_tipo_lugar_view', name='add_tipo_lugar_view'),
     #url(r'^$', 'add_lugar_view', name='add_lugar_view'),
    # url(r'^rutas/', include('rutas.foo.urls')),
    #url(r'^',include('rutas.apps.home.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', admin.site.urls),

    #////////// USUARIOS /////////
    url(r'^reset/password_reset', password_reset, {'template_name':'home/password_reset_form.html', 'email_template_name':'home/password_reset_email.html'}, name='password_reset'),
    url(r'^reset/password_reset_done', password_reset_done, { 'template_name':'home/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb36>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'home/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done', password_reset_complete, {'template_name':'home/password_reset_complete.html'}, name='password_reset_complete'),
    #///////////////////////////// 
]

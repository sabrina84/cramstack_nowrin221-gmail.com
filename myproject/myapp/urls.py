from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = [
    #url(r'^input/', TemplateView.as_view(template_name='signup.html')),
    url(r'^home/', views.contactpage, name='home'),  #start with home
    url(r'^signup/', views.home, name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^gotologin/', views.gotologin, name='gotologin'),
    url(r'^signedup/', views.signup, name='signedup'),
    url(r'^loggedin/', views.login, name='loggedin'),
    url(r'^contactpage/', views.contactpage, name='contactpage'),
    url(r'^addcontact/', views.addcontact, name='addcontact'),
    url(r'^addnewcontact/', views.addnewcontact, name='addnewcontact'),
    url(r'^loggedout/', views.logout, name='loggedout'),
    url(r'^updatecontact/', views.updatecontact, name='updatecontact'),
    url(r'^contactupdated/', views.contactupdated, name='contactupdated'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

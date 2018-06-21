from django.conf.urls import url
from django.contrib import admin
from items import views
from .views import about, contact, home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^about/$', about, name='about'),
    url(r'^contact/$', contact, name='contact')

]
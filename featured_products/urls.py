from django.conf.urls import url
from django.contrib import admin
from items import views
from .views import save_product


urlpatterns = [
    url('^products/save$', save_product, name='save'),

    # url('^blog/(?P<id>\d+)/$', blog_detail, name='detail'),
    # url('^blog/test/$', testing, name='testing'),
]
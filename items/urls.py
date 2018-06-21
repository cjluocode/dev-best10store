from django.conf.urls import url
from .views import search_result


urlpatterns = [
    url('^result/$', search_result, name='result'),
]
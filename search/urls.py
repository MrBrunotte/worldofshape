from django.conf.urls import url
from .views import do_serach

urlpatterns = [
    url(r'^$', do_serach, name='search')
]

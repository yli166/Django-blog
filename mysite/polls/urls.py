from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^polls/',include('polls.urls')),
    url(r'^$',views.index, name = 'index'),
]

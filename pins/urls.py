from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^(?P<pin_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^(?P<pin_id>[0-9]+)/done/$', views.done, name='done'),
]

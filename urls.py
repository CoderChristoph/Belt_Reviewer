from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^books$', views.index),
    url(r'^', views.login),
    url(r'^books/add$', views.add),
    url(r'^books/(?P<id>\d+)$', views.review),
    url(r'^users/(P?<id>\d+)$', views.user),
]
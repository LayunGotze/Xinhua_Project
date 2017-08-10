#coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^logon', views.logon, name='logon'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^analysis', views.analysis, name='analysis'),
]

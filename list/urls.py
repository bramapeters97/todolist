from django.conf.urls import url
from . import views
from django.conf.urls import include
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
    url(r'^todo/(?P<pk>\d+)/$', views.todo_detail, name='todo_detail'),
    url(r'^todo/new/$', views.todo_new, name='todo_new'),
    url(r'^todo/(?P<pk>\d+)/edit/$', views.todo_edit, name='todo_edit'),
]

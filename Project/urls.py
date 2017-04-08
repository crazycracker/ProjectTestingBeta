#!python
# log/urls.py
from django.conf.urls import url, include
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<block_name>\w+)/classrooms$', views.classrooms, name='classrooms'),
    url(r'^(?P<block_name>\w+)/labs$', views.lab, name='lab'),
    url(r'^(?P<block_name>\w+)/classrooms/(?P<room_number>\w+)$', views.roomnumber, name='roomnumber'),
    url(r'^(?P<block_name>\w+)/labs/(?P<room_number>\w+)$', views.labnumber, name='labnumber'),
    # url(r'^cc1/(?P<room_number>\w+)$', views.cc1, name='cc1'),
    url(r'^eventlist$', views.eventlist, name='eventlist'),
    url(r'^auditorium$', views.auditorium, name='auditorium'),
    url(r'^notifications/$', views.notifications, name='notifications'),
    url(r'^nothandler/(?P<pk>\d+)/(?P<status>\d+)/$', views.nothandler, name='nothandler'),
    url(r'^saveEvents$', views.saveEvents, name='saveEvents'),
]

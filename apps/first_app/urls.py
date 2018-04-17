from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register), # build session
    url(r'^login$', views.login), # build session
    url(r'^dashboard$', views.dashboard), 
    url(r'^add$', views.add), #shows template to add a trip
    url(r'^book$', views.book), # this will add a travel plan from the dashboard page when clicking "add travel plan"
    url(r'^join/(?P<id>\d+)$', views.join), # this will add a trip to my trip schedules from another user's built travel plans for specific destination(s)
    url(r'^logout$', views.logout), # del session then redirect
]
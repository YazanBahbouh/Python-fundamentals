from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shows),
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new),
    url(r'^shows/create$', views.create),
    url(r'^shows/(?P<show_id>\d+)$', views.view_show),
    url(r'^shows/(?P<show_id>\d+)/edit$', views.edit_show),
    url(r'^shows/(?P<show_id>\d+)/update$', views.update),
    url(r'^shows/(?P<show_id>\d+)/destroy$', views.destroy)
]
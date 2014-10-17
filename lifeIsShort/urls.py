from django.conf.urls import patterns, url
from lifeIsShort import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

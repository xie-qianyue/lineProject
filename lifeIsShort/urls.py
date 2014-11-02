from django.conf.urls import patterns, url
from lifeIsShort import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_activity/$', views.add_activity),
	url(r'^get_general_report/$', views.get_general_report),
)

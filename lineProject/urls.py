from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lineProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^life/', include('lifeIsShort.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^account/', include('account.urls')),
)

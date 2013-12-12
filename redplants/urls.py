from django.conf.urls import patterns, include, url

from plants import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.specie_list, name='species'),
    url(r'^specie/(\d+)/$', views.specie, name="specie"),

    url(r'^admin/', include(admin.site.urls)),
)

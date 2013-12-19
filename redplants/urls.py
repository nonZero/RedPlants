from django.conf.urls import patterns, include, url

from plants import views

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', views.specie_list, name='species'),
    url(r'^specie/(\d+)/$', views.specie, name="specie"),
    url(r'^like/(\d+)/$', views.like_specie, name="like"),
    url(r'^unlike/(\d+)/$', views.unlike_specie, name="unlike"),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
     {'template_name': 'login.html'}, name='login'),

    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', 
     {'next_page': '/'}),







    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns

from plants import views

from django.contrib import admin
from obs.views import CreateObservationView, ObservationListView
admin.autodiscover()


urlpatterns = i18n_patterns('',
    url(r'^$', views.specie_list, name='species'),
    url(r'^specie/(\d+)/$', views.specie, name="specie"),
    url(r'^like/(\d+)/$', views.like_specie, name="like"),
    url(r'^unlike/(\d+)/$', views.unlike_specie, name="unlike"),


    url(r'^obs/$', ObservationListView.as_view(),
        name="obs"),

    url(r'^post-observation/$', CreateObservationView.as_view(),
        name="post_ob"),


    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
     {'template_name': 'login.html'}, name='login'),

    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', 
     {'next_page': '/'}),

    url(r'^admin/', include(admin.site.urls)),
)

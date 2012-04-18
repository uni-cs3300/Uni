from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

<<<<<<< HEAD
urlpatterns = patterns('',

	url(r'^/adduser/', 'unidjango.views')
=======
urlpatterns = patterns('uni.views',
    (r'^$', 'canvas'),
>>>>>>> Settings, models and url.py
    # Examples:
    # url(r'^$', 'unidjango.views.home', name='home'),
    # url(r'^unidjango/', include('unidjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

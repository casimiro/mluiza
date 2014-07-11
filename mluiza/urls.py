from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from person.api import FacebookUserResource

facebook_user_resource = FacebookUserResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mluiza.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'', include(facebook_user_resource.urls)),
)

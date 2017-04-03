
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^cmsput/$', 'cms.views.give_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(.*)', 'cms.views.index'),
)

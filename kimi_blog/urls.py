from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kimi_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.cover, name='cover'),
    url(r'blog/$', views.blog, name='blog'),
    url(r'blog/(?P<file_name>.+)$', views.blog, name='blog'),
)

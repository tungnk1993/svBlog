"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from myblog import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # test
    url(r'^test_tag/$', views.test_tag),
    url(r'^test_entity/(\d+)/$', views.test_entity),

    # main function
    url(r'^$', views.show_index, name='show_index'),
    url(r'^e/(?P<entity_id>\d+)/$', views.show_entity, name='show_entity'),
    url(r'^e/(?P<entity_id>\d+)/write/$', views.write_review, name='write_review'),
    url(r'^e/(?P<entity_id>\d+)/delete-review/$', views.delete_review),
    url(r'^vote/(?P<review_id>\d+)/(?P<vote_value>\d+)/$', views.change_vote),
    url(r'^profile/$', views.write_profile, name='write_profile'),

    # add, modify entity info
    url(r'^e/(?P<entity_id>\d+)/edit/$', views.edit_info, name='edit_info'),
    url(r'^e/(?P<entity_id>\d+)/add_info/$', views.add_info, name='add_info'),


    # social login
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    
    # basic-login
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^accounts/register/$', views.register, name='register'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
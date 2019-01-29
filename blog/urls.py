from django.conf.urls import url
from django.urls import re_path

from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
]


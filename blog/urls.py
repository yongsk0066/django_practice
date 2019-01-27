from django.conf.urls import url
from django.urls import re_path

from . import views


urlpatterns = [
    url(r'^$', views.post_list),
    re_path(r'^(?P<id>\d+)/$', views.post_detail),
]


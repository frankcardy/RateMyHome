from django.conf.urls import url
from . import views
from django.urls import include, path, re_path

urlpatterns = [

    re_path(r'^$', views.review_list, name='review_list'),

    re_path(r'^review/(P<review_id>[0-9]+)/$', views.review_detail, name = 'review_detail'),

    re_path(r'^home$', views.home_list, name='home_list'),

    re_path(r'^review/(P<home_id>[0-9]+)/$'), views.home_detail, name = 'home_detail')



]

from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index,name="index2"),
    url(r'^signup/$', views.signup,name="signup"),
    url(r'^login/$', views.login,name="login"),
    url(r'^logout/$', views.logout,name="logout"),
    url(r'^menu/(?P<menu_alter>add)$', views.menu,name="menu"),
    url(r'^edit_info/$', views.edit_info,name="edit_info"),
    url(r'^menu_list/$', views.menu_list,name="menu"),
    url(r'^menu/(?P<menu_id>\d+)/$', views.menu_detail,name="menu_detail"),
    url(r'^menu/(?P<menu_alter>alter_\d+)/$', views.menu,name="menu_alter"),
    url(r'^menu/del_(?P<menu_del>\d+)/$', views.menu_delete,name="menu_alter"),
]

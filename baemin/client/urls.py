from django.conf.urls import url,include
from . import views
from partner.views import signup
urlpatterns = [
    url(r'^client$', views.index,name="index"),
    url(r'^$', views.base,name="index"),
    url(r'^client/login/$', views.login,name="index"),
    url(r'^client/logout/$', views.logout,name="logout"),
    url(r'^client/signup/$', signup,name="index"),
    url(r'^client/menu/$', views.menu,name="menu"),
    url(r'^client/orderlist/$', views.order_check,name="menu"),
    url(r'^client/menu_(?P<name>.+)/$', views.menu_list,name="menu"),
    url(r'^client/del_order/$', views.delete_order,name="menu"),
    ]

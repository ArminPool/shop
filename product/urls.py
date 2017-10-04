from django.conf.urls import url, include
from .views import Home, change_items
from .views import detail, category
from . import views

# namespace
app_name = 'product'

urlpatterns = [

    url(r'^$', Home.as_view(), name='home'),
    url(r'^product/(?P<operation>.+)/(?P<pk>\d+)/$', change_items, name='change_item'),
    url(r'^detail/(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^product/(?P<product_category>.+)/$', category, name='category'),
    #   url(r'^comment/add/(?P<pk>\d+)/$', views.add_comment_to_post, name='add_comment_to_post'),
]

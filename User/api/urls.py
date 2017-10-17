from django.conf.urls import url

from User.api.views import UserCreateApiView, UserListApiView, UserDetailApiView, UserBasketApiView

urlpatterns = [
    url(r'^$', UserListApiView.as_view(), name='UserListApi'),
    url(r'^register/$', UserCreateApiView.as_view(), name='create-user'),
    url(r'^detail/(?P<pk>\w+)/$', UserDetailApiView.as_view(), name='user-detail'),
    url(r'^basket/$', UserBasketApiView.as_view(), name='UserBasketApi'),
]
from django.conf.urls import url

from User.api.views import UserCreateApiView, UserListApiView, UserDetailApiView, UserBasketApiView, BasketApiView, \
    BasketUpdateApiView, FileUploadView

urlpatterns = [
    url(r'^$', UserListApiView.as_view(), name='UserListApi'),
    url(r'^register/$', UserCreateApiView.as_view(), name='create-user'),
    url(r'^detail/(?P<pk>\w+)/$', UserDetailApiView.as_view(), name='user-detail'),
    url(r'^basket/$', BasketApiView.as_view(), name='UserBasketApi'),
    url(r'^basket/(?P<pk>\w+)/update', BasketUpdateApiView.as_view(), name='basket-update'),
    url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
]
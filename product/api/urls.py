from django.conf.urls import url
from .views import (PostListApiView,
                    PostDetailApiView,
                    PostDestroyApiView,
                    PostUpdateApiView,
                    CommentDetailApiView, CommentDestroyApiView, CommentUpdateApiView, CommentListApiView)

# namespace


urlpatterns = [

    url(r'^$', PostListApiView.as_view(), name='PostListApi'),
    url(r'^detail/(?P<product_name>[\w+][:/n.]+)/$', PostDetailApiView.as_view(), name='post-detail'),
    url(r'^detail/(?P<product_name>\w+)/delete/$', PostDestroyApiView.as_view(), name='post-delete'),
    url(r'^detail/(?P<product_name>\w+)/edit/$', PostUpdateApiView.as_view(), name='post-update'),

    url(r'^comments/$', CommentListApiView.as_view(), name='CommentListApi'),
    url(r'^comments/(?P<pk>\w+)/$', CommentDetailApiView.as_view(), name='comment-detail'),
    url(r'^comments/(?P<pk>\w+)/delete/$', CommentDestroyApiView.as_view(), name='comment-delete'),
    url(r'^comments/(?P<pk>\w+)/edit/$', CommentUpdateApiView.as_view(), name='comment-update'),

]

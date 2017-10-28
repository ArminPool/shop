from django.db.models import Q
from rest_framework import request
from rest_framework.generics import \
    (ListAPIView,
     RetrieveAPIView,
     UpdateAPIView,
     DestroyAPIView,
     RetrieveUpdateAPIView,
     )

from rest_framework.permissions import \
    (AllowAny,
     IsAdminUser,
     IsAuthenticated,
     IsAuthenticatedOrReadOnly)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from product.api.pagination import PostLimitOffsetPagination
from product.api.serializer import PostListSerializer, CommentListSerializer, PostDetailSerializer, \
    CommentDetailSerializer
from product.models import Post, Comment
from .permissions import IsOwnerOrReadOnly


class PostDetailApiView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    lookup_field = 'product_name'


class PostListApiView(ListAPIView):
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    pagination_class = PostLimitOffsetPagination
    search_fields = ['product_name','product_prize']
    ordering = ('-product_prize',)

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(product_name__icontains=query) |
                Q(product_prize__icontains=query) |
                Q(product_category__icontains=query)
            ).distinct()

        return queryset_list


class PostUpdateApiView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'product_name'


class PostDestroyApiView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = PostListSerializer
    lookup_field = 'product_name'


class CommentListApiView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer



class CommentDetailApiView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentUpdateApiView(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]


class CommentDestroyApiView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer

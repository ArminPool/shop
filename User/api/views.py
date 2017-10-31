from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import views
from rest_framework.generics import \
    (ListAPIView,
     RetrieveAPIView,
     UpdateAPIView,
     DestroyAPIView,
     RetrieveUpdateAPIView,
     CreateAPIView)
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser

from rest_framework.permissions import \
    (AllowAny,
     IsAdminUser,
     IsAuthenticated,
     IsAuthenticatedOrReadOnly)
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from User.api.permissions import UserDetailPermissions, IsOwnerOfBasket
from User.api.serializer import CreateUserSerializer, UserListSerializer, UserDetailSerializer, UserBasketSerializer, \
    BasketSerializer, UserImageSerializer
from User.models import UserProfile
from product.api.pagination import PostLimitOffsetPagination
from product.api.serializer import PostListSerializer, CommentListSerializer, PostDetailSerializer, \
    CommentDetailSerializer, FileUploadSerializer
from product.models import Basket, FileUpload

User = get_user_model()


class UserListApiView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAdminUser]


class UserCreateApiView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class UserDetailApiView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [UserDetailPermissions]


class UserBasketApiView(RetrieveAPIView):
    queryset = Basket.objects.all()
    serializer_class = UserBasketSerializer
    permission_classes = [IsOwnerOfBasket]


class BasketUpdateApiView(RetrieveUpdateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsOwnerOfBasket]


class BasketApiView(ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [IsAdminUser]


class FileUploadView(CreateAPIView):
    queryset = FileUpload.objects.all()
    parser_classes = (FileUploadParser,)

    serializer_class = UserImageSerializer

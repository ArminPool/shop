from django.contrib.auth import get_user_model
from rest_framework import request
from rest_framework.reverse import reverse
from rest_framework.serializers import (
    ModelSerializer
, HyperlinkedIdentityField,
    SerializerMethodField,
)

from ..models import Post, Comment


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api-posts:post-detail',
        lookup_field='product_name'
    )

    class Meta:
        model = Post
        fields = ['product_name', 'product_prize', 'url', ]


class PostDetailSerializer(ModelSerializer):
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = ['product_name', 'product_prize', 'product_category', 'comments']

    def get_comments(self, obj):
        return CommentDetailSerializer(obj.comments, many=True).data




class CommentListSerializer(ModelSerializer):
    user = SerializerMethodField()
    post = SerializerMethodField()
    url = HyperlinkedIdentityField(
        view_name='api-posts:comment-detail',

    )

    class Meta:
        model = Comment
        fields = ['id','post', 'user', 'body', 'url']

    def get_user(self, obj):
        return str(obj.user.username)

    def get_post(self, obj):
        return str(obj.post)


class CommentDetailSerializer(ModelSerializer):
    post = SerializerMethodField()
    replies = SerializerMethodField()
    user = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id','post', 'user', 'body', 'replies',]

    def get_user(self, obj):
        return str(obj.user.username)

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildrenSerializer(obj.children(), many=True).data
        return None

    def get_post(self, obj):
        return str(obj.post)




class CommentChildrenSerializer(ModelSerializer):
    post = SerializerMethodField()
    user = SerializerMethodField()


    class Meta:
        model = Comment
        fields = ['id','post', 'user', 'body', 'user']

    def get_user(self, obj):
        return str(obj.user.username)

    def get_post(self, obj):
        return str(obj.post)

import re

from django.contrib.auth import get_user_model
from django.forms import PasswordInput
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    ModelSerializer
, HyperlinkedIdentityField,
    SerializerMethodField,
    CharField

)

from User.models import UserProfile
from product.models import Basket

User = get_user_model()


class UserListSerializer(ModelSerializer):
    username = SerializerMethodField()
    url = HyperlinkedIdentityField(
        view_name='api-users:user-detail',

    )

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'url']

    def get_username(self, obj):
        return obj.user.username


class CreateUserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['user', 'phone_number', 'city', 'website', 'pro_img']


class CreateUserSerializer(ModelSerializer):
    username = CharField(max_length=15, )
    phone_number = CharField(max_length=15, )

    password1 = CharField(
        style={'input_type': 'password'}
    )
    password2 = CharField(
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']
        extra_kwargs = {"password1":
                            {"write_only": True}
                        }

    def validate_username(self, value):
        username = value
        if User.objects.filter(username=username):
            raise ValidationError("این نام کاربری وجود دارد.")
        return value

    def validate_phone_number(self, value):
        phone_number = value
        regex = r'0\d{10}'
        if not re.match(regex, phone_number):
            raise ValidationError('!!!شماره تلفن درست وارد نشده')
        return value

    def validate_password2(self, value):
        data = self.get_initial()
        password1 = data.get('password1')
        password2 = value

        if password1 == password2:
            return value
        raise ValidationError("تکرار رمز عبور صحیح نیست.")

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password1 = validated_data['password1']
        password2 = validated_data['password2']
        phone_number = validated_data['phone_number']

        user_obj = User(
            username=username,
            email=email

        )
        user_obj.set_password(password1)
        user_obj.save()
        userprofile = UserProfile.objects.create(

            user=user_obj
        )
        userprofile.phone_number = phone_number
        userprofile.save()
        return validated_data


class UserDetailSerializer(ModelSerializer):
    username = SerializerMethodField()
    email = SerializerMethodField()
    basket = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'phone_number', 'city', 'website', 'pro_img','basket']

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email
    def get_basket(self, obj):
        return UserBasketSerializer(obj.user.basket,many=True).data


class UserBasketSerializer(ModelSerializer):
    product_name = SerializerMethodField()

    class Meta:
        model = Basket
        fields = ['current_user', 'product_name']

    def get_product_name(self,obj):
        games = []
        for field in obj.product_name.all():
            games.append(field.product_name)
        return games



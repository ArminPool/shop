from django.contrib.auth.models import User
from django.db import models


# Create Posts Models for Product which we want to add in our site
class Post(models.Model):
    product_name = models.CharField(max_length=250)

    product_prize = models.CharField(max_length=250)

    product_img = models.FileField(null=True, blank=True, upload_to='uploaded')

    product_des = models.TextField(max_length=2000)

    product_category = models.CharField(max_length=250)

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return self.product_name


# Each User have a Basket for buying the Products
class Basket(models.Model):
    product_name = models.ManyToManyField(Post,)

    current_user = models.ForeignKey(User, related_name='basket')

    @classmethod
    def add_item(cls, current_user, new_item):
        # We check our user already have a basket or not, if not we create one for him

        basket, create = cls.objects.get_or_create(

            current_user=current_user
        )

        basket.product_name.add(new_item)

    @classmethod
    def remove_item(cls, current_user, new_item):
        basket, created = cls.objects.get_or_create(

            current_user=current_user
        )

        basket.product_name.remove(new_item)


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)

        return qs


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    user = models.ForeignKey(User, null=True)
    body = models.TextField(max_length=250, null=True)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    parent = models.ForeignKey("self", null=True, blank=True)
    public = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):

        return self.user.username

    def is_parent(self):
        if self.parent is not None:
            return False
        return True

    # is_public for moderation
    def is_public(self):

        if self.public:
            return True
        return False

    def children(self):
        return Comment.objects.filter(parent=self)

class FileUpload(models.Model):

    img = models.FileField(null=True,upload_to='uploaded')
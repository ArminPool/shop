from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django.db import models
from django.db.models import ManyToManyField

from .models import Post, Basket, Comment, FileUpload
from User.models import UserProfile, UsersMessage, GuestMessage
from django.forms import TextInput, Textarea


# Here we customize AdminModel
class AdminModel(admin.ModelAdmin):

    formfield_overrides = {

        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }




# add models to admin page
admin.site.register(Post, AdminModel)
admin.site.register(Basket)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(GuestMessage)
admin.site.register(UsersMessage)
admin.site.register(FileUpload)


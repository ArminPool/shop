from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models


class UserProfile(models.Model):
    # Each user-field in UserProfile can only have one user
    user = models.OneToOneField(User, related_name="userprofile", null=True)
    phone_number = models.CharField(max_length=11, blank=False)

    city = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    pro_img = models.FileField(null=True, blank=True, upload_to='uploaded')

    def __str__(self):
        if self.user:
            return self.user.username
        return "unknown"

    @classmethod
    def create_profile(cls, user, phone_number):
        userprofile = cls.objects.create(

            user=user
        )
        userprofile.phone_number = phone_number
        userprofile.save()


"""
Note: Receiver of UsersMessage and GuestMessage is admin  cuz we don't need chat between users in a shop 

"""


# Here is Contact for Guest that i said before
class UsersMessage(models.Model):
    author = models.OneToOneField(User, related_name="author", null=True, blank=True)

    cooperate = 'co'
    problem_buying = 'pb'
    ask_game = 'ag'
    others = 'o'

    options = (
        (cooperate, 'همکاری'), (problem_buying, 'مشکل در خرید'), (ask_game, 'درخواست بازی'), (others, 'موارد دیگر'))
    issue_options = models.CharField(choices=options, default=cooperate, max_length=2)
    message = models.TextField(max_length=250, null=True)

    def __str__(self):
        return str(self.author) + " " + str(self.issue_options)


# Here is Contact for Guest that i said before
class GuestMessage(models.Model):
    Guest_first_name = models.CharField(max_length=10, null=True)
    Guest_last_name = models.CharField(max_length=10, null=True)
    Guest_email = models.EmailField(max_length=50, null=True)
    cooperate = 'co'
    problem_buying = 'pb'
    ask_game = 'ag'
    others = 'o'

    options = (
        (cooperate, 'همکاری'), (problem_buying, 'مشکل در خرید'), (ask_game, 'درخواست بازی'), (others, 'موارد دیگر'))
    issue_options = models.CharField(choices=options, default=cooperate, max_length=2)
    message = models.TextField(max_length=250, null=True)

    def __str__(self):
        return str(self.Guest_first_name) + " " + str(self.issue_options)

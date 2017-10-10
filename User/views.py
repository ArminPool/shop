import pytz
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from User.form import RegistrationForm, ProfileForm

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required

from User.models import UserProfile
from product.models import Basket, Post

"""
This is what really needs to be explained:
I didn't want to customize django.contrib.auth.User and also i wanted to have phone_number in
registration form and The problem was that there was a field in another form and we haven't a 
UserProfile for user until we create The user.And because of that i first saved user form then 
create a profile for that user and set null=True inside user field in UserProfile Model.

"""


def register(request):
    if request.method == 'POST':

        form1 = RegistrationForm(request.POST)
        form2 = ProfileForm(request.POST)

        if form1.is_valid() and form2.is_valid():

            phone_number = form2.cleaned_data['phone_number']
            user = form1.save()

            UserProfile.create_profile(user, phone_number)
            login(request, user)

            return redirect(reverse('product:home'))

        else:
            print("lvl1")

            form1 = RegistrationForm(request.POST)
            form2 = ProfileForm(request.POST)

            args = {'form1': form1, 'form2': form2,}
            return render(request, 'User/reg_form.html', args)
    else:
        form1 = RegistrationForm()
        form2 = ProfileForm()
        args = {'form1': form1, 'form2': form2}
        return render(request, 'User/reg_form.html', args)


@login_required
def view_profile(request):
    all_posts = Post.objects.all()
    users = User.objects.get(id=request.user.id)
    try:
        item = Basket.objects.get(current_user=request.user)
        items = item.product_name.all()
        args = {'user': request.user, 'items': items, 'users': users, 'all_posts': all_posts,'timezones': pytz.common_timezones}
        return render(request, 'User/profile.html', args)

    except:

        args = {'user': request.user, 'users': users, 'all_posts': all_posts,'timezones': pytz.common_timezones}
        return render(request, 'User/profile.html', args)


# request.FILES is for save uploaded picture
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            print("success")
            form.save()
            return redirect('/user/profile')

        else:

            form = ProfileForm(instance=request.user.userprofile)
            args = {'form': form, }
            return render(request, 'User/edit_profile.html', args)
    else:
        form = ProfileForm(instance=request.user.userprofile)
        args = {'form': form}
        return render(request, 'User/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/user/profile')
        else:
            return redirect('/user/change-password')

    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'User/change_password.html', args)

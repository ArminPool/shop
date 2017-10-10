from django.shortcuts import render, redirect

from django.views.generic import ListView
import pytz

from User.form import ContactForm, UsersContactForm
from product.form import CommentForm
from .models import Post, Basket, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'product/timezone.html', {'timezones': pytz.common_timezones})


class Home(ListView):
    # In this template we show all posts.
    model = Post
    template_name = 'product/posts.html'
    context_object_name = 'posts'
    # For pagination more detail www.simplebetterthancomplex.com
    paginate_by = 6
    queryset = Post.objects.all()


def category(request, product_category):
    posts_list = Post.objects.filter(product_category=product_category)

    paginator = Paginator(posts_list, 6)
    template_name = 'product/results.html'
    page = request.GET.get('page', 1)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'posts': posts, 'category': product_category}
    return render(request, template_name, context)


"""
Here we have two Contact one for Users and another for Guests with two different form and two different template
"""


def contact(request):
    users_template_name = 'product/UsersContact.html'
    guest_template_name = 'product/GuestContact.html'
    if request.method == 'POST':

        if request.user.is_authenticated:

            form = UsersContactForm(request.POST)
            if form.is_valid():
                # use print for debugging
                print('valid-users-form')
                usermassage = form.save(commit=False)
                usermassage.author = request.user
                form.save(commit=True)
                return redirect('product:home')
            else:
                print('invalid-users-form')

                print('authenticated')
                form = UsersContactForm()
                return render(request, users_template_name, {'form': form})
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                print('guest-valid')
                form.save()
                return redirect('product:home')
            else:
                print('guest-invalid')

                form = ContactForm()
                return render(request, guest_template_name, {'form': form})

    else:
        if request.user.is_authenticated:

            print('authenticated')
            form = UsersContactForm()
            return render(request, users_template_name, {'form': form})
        else:

            form = ContactForm()
            return render(request, guest_template_name, {'form': form})


def about_us(request):
    template_name = 'product/about-us.html'
    return render(request, template_name)


def advertising(request):
    template_name = 'product/advertising.html'
    return render(request, template_name)


# Maybe our Users want to change their basket of games
def change_items(request, operation, pk):
    new_item = Post.objects.get(pk=pk)

    if operation == 'add':
        Basket.add_item(request.user, new_item)

    if operation == 'remove':
        Basket.remove_item(request.user, new_item)

    return redirect('product:home')


# Each product most have extra information
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            try:
                parent_id = int(request.POST.get("parent_id"))

            except:
                parent_id = None
                print("error")

            if parent_id:
                comment.parent = Comment.objects.get(pk=parent_id)

            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('product:detail', pk=post.pk)
    else:
        form = CommentForm()
    template_name = 'product/details.html'
    context = {'form': form, 'post': post}
    return render(request, template_name, context)

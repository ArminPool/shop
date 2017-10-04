from django.conf.urls import url

import product
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete

from product import views as PV

app_name = 'user'
urlpatterns = [
    url(r'^$', PV.Home.as_view()),

    # Allows to render our own login page
    url(r'^login/$', login, {'template_name': 'User/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'User/logout.html'}),
    url(r'register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, {'template_name': 'User/reset_password.html',
                                               'post_reset_redirect': 'user:password_reset_done',
                                               'email_template_name': 'User/reset_password_email.html'},
        name='reset_password'),

    url(r'^reset-password-done$', password_reset_done, {'template_name': 'User/reset_password_done.html'},
        name='password_reset_done'),
    # url(r'^reset-password/confirm$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
        {'template_name': 'User/reset_password_confirm.html',
         'post_reset_redirect': 'user:password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete$', password_reset_complete,
        {'template_name': 'User/reset_password_complete.html'}, name='password_reset_complete'),

]

# url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,
#     name='password_reset_confirm')

# python -m smtpd -n -c DebuggingServer localhost:1025
# and adjust your mail settings accordingly:
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = 1025

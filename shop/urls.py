from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

from product.views import contact, about_us, advertising, set_timezone,Search
from shop import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    url(r'', include('product.urls')),
    url(r'^user/', include('User.urls')),
   # url(r'^search/', include('haystack.urls')),
    url(r'^search/', Search,name='search'),

    url(r'^contact/$', contact, name='Contact'),
    url(r'^about-us/$', about_us, name='about-us'),
    url(r'^advertising/$', advertising, name='advertising'),
    url(r'^timezone/$', set_timezone, name='timezone'),
    url(r'^api/posts/', include('product.api.urls', namespace='api-posts')),
    url(r'^api/users/', include('User.api.urls', namespace='api-users')),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
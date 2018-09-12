"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
# RedirectView will allow us to redirect to a view
from django.views.generic import RedirectView
from django.views.static import serve
# MEDIA_ROOT will allow us to serve our media url
from .settings import MEDIA_ROOT

# Once we've imported all we need, we add to the urlpatterns list

urlpatterns = [
    url(r'admin/', admin.site.urls),
    # If somebody goes to the root directory of our project, we want to redirect
    # them to 'posts'
    url(r'^$', RedirectView.as_view(url='posts/')),
    # If somebody goes to the 'posts' url, then, we want it to be passed using 
    # the URLs in the urls.py file in the posts app.
    url(r'posts/', include('posts.urls')),
    # For media, we indicate the start of a line with media, and using the 
    # regular expression below, we can point towards a path to a particular file
    # then we use the 'serve' library and we serve up the document_root MEDIA_ROOT
    # that we imported from our settings earlier
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

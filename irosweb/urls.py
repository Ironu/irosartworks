"""irosweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from apps.galeria_app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('sculpts/', views.sculpts, name='sculpts'),
    path('contact/', views.contact, name='contact'),
    path('base', views.base, name='base'),
    path('illustrations/', views.illustrations, name='illustrations'),
    path('tresD/', views.tresD, name='tresD'),
    path('mail/', views.mail, name='mail'),
    #path('comentario/<int:id >/approve', views.comment_aprove, name=comment_aprove),
    #path('comentario/<int:id >/remove', views.comment_remove, name=comment_remove),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
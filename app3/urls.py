"""app3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app3 import views
from app3.views import Ingrediant_image_view, success, display_ingrediant_images

# TEMPLATE TAGGING
app_name = 'app_3'

urlpatterns=[
    path('image_upload/', Ingrediant_image_view, name = 'image_upload'),
    path('success/', success, name = 'success'),
    path('hotel_images/', display_ingrediant_images, name = 'hotel_images'),
    path('other/',views.Ingrediant_image_view,name='other'),
    path('relative/',views.relative,name='relative'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

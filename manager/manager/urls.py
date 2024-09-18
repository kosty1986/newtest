"""
URL configuration for manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from hr.views import home_page, contact_page, upload_page, send_email_page, RegisterViewSet

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from catalog.views import ProductViewSet


router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet, 'register')
router.register(r'products', ProductViewSet, 'products')

urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('users/', include('users.urls', namespace='users')),
    path('',home_page,name='home'),
    path('contact/',contact_page, name='contact'),
    path('upload/',upload_page, name='upload'),
    path('send_email/',send_email_page, name='send_email'),
    # path('register/',register_page, name='register'),


    path('api/', include(router.urls),name='api'),
    path('api/auth/', jwt_views.TokenObtainPairView.as_view(), name='api-auth'),
    path('api/auth/refresh/', jwt_views.TokenRefreshView.as_view(), name='api-auth-refresh'),

]

if settings.DEBUG is True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
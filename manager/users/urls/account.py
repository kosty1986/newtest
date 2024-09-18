from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import register_view


app_name = 'account'
urlpatterns= [
#     # path('', include('django.contrib.auth.urls')),
#     path('', include('users.urls.account')),
    path('register/', register_view, name='register'),
    path('activation/<str:token>', include('users.urls.activation'))
 ]
# urlpatterns= [
#     path('register/', register_view, name='register'),
#     path('', include('django.contrib.auth.urls'))
#
# ]


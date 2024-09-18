from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import register_view
from users.views.activation import activate_user,reset_token_view

app_name = 'activation'
urlpatterns= [
     path('activate', activate_user, name='activate'),
     path('reset_token/', reset_token_view, name='reset_token')

 ]

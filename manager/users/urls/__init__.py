from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('account/', include('users.urls.account')),
    path('activation/', include('users.urls.activation')),
]

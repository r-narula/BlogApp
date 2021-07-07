from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',views.register,name='blog-register'),
    path('drf/',views.users_list,name="Users-list!"),
    path('profile/',views.profile,name="blog-profile"),
    path('login/',auth_views.LoginView.as_view(template_name="Users/login.html"),name="blog-login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="Users/logout.html"),name="blog-logout"),
]
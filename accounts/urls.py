from django.conf import settings
from django.conf.global_settings import LOGIN_URL
from django.conf.urls import url
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from accounts import views



urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),

    path('login/', views.login, name='login'),

    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login_form.html', authentication_form= LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=LOGIN_URL), name='logout'),

]
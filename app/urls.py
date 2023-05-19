from django.contrib.auth import views
from django.urls import path

from .views import main_page, signup

urlpatterns = [
        path('', main_page, name='main_page'),
        path('signup/', signup, name='signup'),
        path('login/', views.LoginView.as_view(template_name='app/login.html'), name='login'),
        path('logout/', views.LogoutView.as_view(), name='logout'), 
    ]
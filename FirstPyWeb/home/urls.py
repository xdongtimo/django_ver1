from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name= 'home'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('/',auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
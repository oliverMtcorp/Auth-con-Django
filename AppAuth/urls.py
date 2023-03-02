from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('welcome/', views.welcome, name='welcome'),
    path("login_firebase", views.login_firebase),
    path("login", views.login),
    path("login_google", views.login_google),
]
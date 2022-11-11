from django.urls import path
from .import views
from knox import views as baseviews

urlpatterns = [
    path("register/", views.RegisterView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("logout/", baseviews.LogoutView.as_view()),
]

from django.urls import path, include
from . import views
urlpatterns = [
    path("<int:pk>/", views.UserDetailView.as_view()),
]

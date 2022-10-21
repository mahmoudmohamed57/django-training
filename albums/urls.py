from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('create', login_required(views.create.as_view()), name='create'),
]

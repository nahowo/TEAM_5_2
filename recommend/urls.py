from django.urls import path
from django.contrib import admin
from .views import RandomTeamsView

urlpatterns = [
    path(r'recommend/', RandomTeamsView.as_view()),
]
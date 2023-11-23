from django.urls import path
from django.contrib import admin
from .views import RandomTeamsView

urlpatterns = [
    path('', RandomTeamsView.as_view()),
]
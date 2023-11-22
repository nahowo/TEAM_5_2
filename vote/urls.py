from django.urls import path
from django.contrib import admin
from .views import TeamViewSet, VoteView

urlpatterns = [
    path('', TeamViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', TeamViewSet.as_view({'get': 'retrieve'})),
    path('<int:team_id>/', VoteView.as_view()),
]
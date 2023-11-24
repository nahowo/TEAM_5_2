from django.urls import path
from django.contrib import admin
from .views import TeamViewSet, VoteView

urlpatterns = [
    path('vote/', TeamViewSet.as_view({'get': 'list'})),
    path('vote/<int:pk>/', TeamViewSet.as_view({'get': 'retrieve'})),
    # path('vote/<int:team_id>/', VoteView.as_view({'patch': 'update'})),
    path('vote/<int:team_id>', VoteView.as_view()),
]
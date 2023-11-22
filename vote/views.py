from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class VoteView(APIView):
    def post(self, request, team_id, format=None):
        team = Team.objects.get(id=team_id)
        team.voted += 1
        team.save()
        return Response({'status': 'vote counted'})
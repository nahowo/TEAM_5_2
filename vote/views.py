from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class VoteView(APIView):
    def patch(self, request, team_id):
        team = Team.objects.get(id=team_id)
        team.votes += 1
        team.save()

        return Response({
            'status': status.HTTP_200_OK,
            'team_name': team.name,
            'votes': team.votes
        })
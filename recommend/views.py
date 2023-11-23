from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Team
from .serializers import TeamSerializer
import random

class RandomTeamsView(APIView):
    def get(self, request, format=None):
        count = request.query_params.get('count', 1)
        count = int(count)
        teams = list(Team.objects.all())
        random.shuffle(teams)
        teams = teams[:count]
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)
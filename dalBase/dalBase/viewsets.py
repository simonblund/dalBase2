from rest_framework import viewsets
from .models import Incident
from .serializers import IncidentSzs


class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSzs

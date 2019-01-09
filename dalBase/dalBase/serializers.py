from rest_framework import serializers
from .models import Incident


class IncidentSzs(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'



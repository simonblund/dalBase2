from rest_framework import routers
from dalBase.viewsets import IncidentViewSet

router = routers.DefaultRouter()

router.register(r'incident', IncidentViewSet)

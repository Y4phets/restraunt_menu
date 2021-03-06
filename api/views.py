from meals.models import Meals
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import MealSerializer


class MealsView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Meals.objects.all()
    serializer_class = MealSerializer

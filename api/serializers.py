from rest_framework import serializers

from meals.models import Meals


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = ("name", "proteins", "fats", "carbohydrates", "calories",
                  "price", "picture", "allergens", "category",)

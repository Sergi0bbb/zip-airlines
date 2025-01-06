from rest_framework import serializers
from airlines_app.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = ["id", "amount_of_passengers"]


class AirplaneDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = [
            "id",
            "amount_of_passengers",
            "fuel_tank_capacity",
            "fuel_consumption_per_minute",
            "fuel_consumption_per_minute_with_passengers",
            "fly_max_time"
        ]

from math import log

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from airlines_app.models import Airplane


class TestAirplaneModel(TestCase):
    def test_airplane_methods(self):
        airplane = Airplane.objects.create(amount_of_passengers=15)

        expected_fuel_tank_capacity = round(airplane.id * 200, 2)
        expected_fuel_consumption_per_minute = round(log(airplane.id) * 0.80, 2)
        expected_fuel_consumption_with_passengers = round(expected_fuel_consumption_per_minute + (15 * 0.002), 2)
        expected_fly_max_time = round(expected_fuel_tank_capacity / expected_fuel_consumption_with_passengers,2)

        self.assertEqual(airplane.fuel_tank_capacity,expected_fuel_tank_capacity)
        self.assertEqual(airplane.fuel_consumption_per_minute,expected_fuel_consumption_per_minute)
        self.assertEqual(airplane.fuel_consumption_per_minute_with_passengers,expected_fuel_consumption_with_passengers)
        self.assertEqual(airplane.fly_max_time, expected_fly_max_time)


class TestAirplaneViewSet(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.airplane_data = {"amount_of_passengers": 150}

    def test_create_airplane_success(self):
        response = self.client.post("/api/v1/zip_airlines/airplanes/", [self.airplane_data], format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Airplanes created!")

    def test_create_airplane_exceeds_limit(self):
        response = self.client.post("/api/v1/zip_airlines/airplanes/", [self.airplane_data] * 11, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(response.data["error "], "You can create only 10 airplanes!")

from django.db import models
from math import log


class Airplane(models.Model):
    amount_of_passengers = models.PositiveIntegerField(default=0)

    @property
    def fuel_tank_capacity(self) -> int:
        return round(self.id * 200, 2)

    @property
    def fuel_consumption_per_minute(self) -> float | int:
        return round(log(self.id) * 0.80, 2)

    @property
    def fuel_consumption_per_minute_with_passengers(self) -> float | int:
        return round(self.fuel_consumption_per_minute +
                     (self.amount_of_passengers * 0.002), 2)

    @property
    def fly_max_time(self) -> float | int:
        return round(self.fuel_tank_capacity /
                     self.fuel_consumption_per_minute_with_passengers, 2)

    @property
    def __str__(self):
        return (f"Airplane {self.id} with "
                f"{self.amount_of_passengers} passengers")

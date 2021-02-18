from django.db import models


# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    engine_size = models.IntegerField()
    fuel_type = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.make} {self.model} - {self.engine_size} {self.fuel_type}'

    # def serialize(self):
    #     return {
    #         'make': self.make,
    #         'model': self.model,
    #         'engine_size': self.engine_size,
    #         'fuel_type': self.fuel_type
    #     }

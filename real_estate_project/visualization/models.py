# visualization/models.py

from django.db import models

class Realtor(models.Model):
    brokered_by = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    price = models.FloatField()
    bed = models.FloatField()
    bath = models.FloatField()
    acre_lot = models.FloatField()
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    house_size = models.FloatField()
    prev_sold_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state} - ${self.price}"

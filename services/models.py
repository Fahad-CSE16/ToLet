from django.db import models
from django.contrib.auth.models import User
class VehicleServe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='services')
    vehicle_type=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=200)
    destination=models.CharField(max_length=200)
    def __str__(self):
        return self.user.username + "" + self.location + "To " + self.destination


from django.db import models
from buildings.models import District
from django.contrib.auth.models import User
class VehicleServe(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, related_name='services')
    vehicle_type=models.CharField(max_length=100)
    phone=models.CharField(max_length=17)
    company_name=models.CharField(max_length=100)
    location=models.ForeignKey(District, on_delete=models.SET_NULL, related_name='district_set',null=True)
    labour=models.IntegerField()
    def __str__(self):
        return self.user.username + " " + self.location.name 


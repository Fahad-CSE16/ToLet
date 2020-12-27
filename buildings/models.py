from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.timezone import now

class District(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Flat(models.Model):
    RENTTYPE=(
        ('Family','Family'),
        ('Bachelor','Bachelor'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feeds')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='districts_set')
    address=models.TextField()
    phone = models.CharField(max_length=17)
    total_stairs=models.IntegerField()
    floor=models.IntegerField()
    lift=models.BooleanField(default=False)    
    gas=models.BooleanField(default=False)    
    parking=models.BooleanField(default=False)  
    is_available=models.BooleanField(default=True)  
    size=models.FloatField()  
    rent_type = models.CharField(max_length=50, choices=RENTTYPE)
    rent=models.IntegerField()
    details=models.TextField(blank=False, max_length=500)
    timestamp=models.DateTimeField(default=now)
    photo = models.ImageField(upload_to="Buildings/images")
    def save( self, *args, **kwargs):
        super(Flat, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)
 
        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)

    
class FlatImages(models.Model):
    photo = models.ImageField(upload_to="Buildings/images")
    flat = models.ForeignKey(
        Flat, on_delete=models.CASCADE, related_name='images')
    def save( self, *args, **kwargs):
        super(FlatImages, self).save(*args, **kwargs)
        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)


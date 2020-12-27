from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User,AbstractUser
from PIL import Image
from multiselectfield import MultiSelectField
class UserProfile(models.Model):
    GENRE_CHOICES = (
        ('Male', 'MALE'),
        ('Female', 'FEMALE'),
    )
    CATEGORY=(
        ('Owner', 'Owner'),
        ('Tenant', 'Tenant'),
        ('Servant', 'Servant'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=50, choices=GENRE_CHOICES)
    address = models.CharField(max_length=150)
    phone=models.CharField(max_length=13)
    profession=MultiSelectField(max_length=100,choices=CATEGORY,null=True,max_choices=2)
    image=models.ImageField(default='default.jpg', upload_to='tuition/images')

    def __str__(self):
        return f'{self.user.username} Profile'
    AUTH_PROFILE_MODULE = 'app.UserProfile'
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100, blank=True,null=True)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank= True)
    def __str__(self):
        return 'message from '+ self.name +' - '+ self.email

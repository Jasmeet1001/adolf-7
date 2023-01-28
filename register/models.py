from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from PIL import Image

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_adolf_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("SuperUser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("SuperUser must have is_superuser=True.")
        return self.create_user(phone_number, password, **extra_fields)

class User(AbstractUser):
    username = None
    phone_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField(blank=True)
    is_adolf_staff = models.BooleanField("Adolf7 Admin", default=False)
    is_distributer = models.BooleanField("Distributer", default=False)
    is_retailer = models.BooleanField("Retailer", default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     photo = models.FileField(default='default.jpg', upload_to='profile_pics')
#     location = models.CharField(max_length=250)

#     def __str__(self):
#         return f"{self.user.first_name} {self.user.last_name} Profile"
    
#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

#         img = Image.open(self.photo.path)

#         if img.height > 300 or img.width > 300:
#             resize = (300, 300)
#             img.thumbnail(resize)
#             img.save(self.photo.path)

import uuid

from django.db import models
from users.models import *
from .consts import *
from .utils import user_listing_path


# Create your models here.
class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=24, choices=CAR_BRANDS, default=None)
    # vin = models.CharField(max_length=17)
    mileage = models.ImageField(default=0)
    color = models.CharField(max_length=24, default='white')
    description = models.TextField()
    engine = models.CharField(max_length=24, default='')
    transmission = models.CharField(max_length=24, choices=TRANSMISSION_OPTION, default=None)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    # NB on_delete above not working when SET_NULL
    image = models.ImageField(upload_to=user_listing_path)

from django.db import models
from django.utils.timezone import now
from realtors.models import Realtor
from django.conf import settings

class Listing(models.Model):

    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'for rent'
        
    class HomeType(models.TextChoices):
        HOUSE = 'house'
        CONDO = 'condo'
        TOWNHOUSE = 'TownHouse'

    realtor = models.ForeignKey(Realtor , on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices = SaleType.choices , default = SaleType.FOR_SALE)
    price = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    home_type = models.CharField(max_length=50, choices=HomeType.choices, default=HomeType.HOUSE)
    sqft = models.FloatField()
    open_house = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='listing_photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)

    @property
    def getListingPhotosCount(self):
        return ListingPhoto.objects.filter(listing = self.id).count() + 1 ## +1 for the main photo

    @property
    def getListingPhotos(self):
        return  ListingPhoto.objects.filter(listing = self.id).count() 
    
    def __str__(self):
        return self.title

    



class ListingPhoto(models.Model):
    photo = models.ImageField(upload_to='listing_photos/%Y/%m/%d/')
    listing =  models.ForeignKey(Listing , related_name = "listing_photos", on_delete=models.DO_NOTHING)

    @property
    def photo_url(self):
        return "{0}{1}".format('http://127.0.0.1:8000' ,self.photo.url)
    def __str__(self):
        return "photo of " + str(Listing.title)

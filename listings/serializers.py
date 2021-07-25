from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Listing

class ListingSerializer(ModelSerializer):
    listing_photos =  listing_photos = serializers.SlugRelatedField(many=True, read_only=True, slug_field="photo_url")
    class Meta:
        model = Listing
        fields = ('title', 'address','city','state','price','sale_type',
                'home_type','bedrooms','bathrooms','sqft','photo_main','slug','listing_photos')




class ListingDetailSerializer(ModelSerializer):
    # PrimaryKeyRelatedField
    listing_photos = serializers.SlugRelatedField(many=True, read_only=True, slug_field="photo_url")
  
    class  Meta:
        model = Listing
        fields = ('realtor','title', 'address','city','state','price','sale_type',
                'home_type','bedrooms','bathrooms','sqft','photo_main','slug','listing_photos',
                'description', 'zipcode','list_date')

        lookup_field='slug' ## will be used for search and as a parameter to the mapping url
        

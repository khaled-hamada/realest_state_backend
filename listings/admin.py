from django.contrib import admin
from .models import Listing, ListingPhoto

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'price','list_date','realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address','city','state','zipcode','price')
    list_per_page = 25
class ListingPhotoAdmin(admin.ModelAdmin):
    list_display = ('id','listing','photo')
    list_display_links = ('id',)
    list_filter = ('listing__title',)
    search_fields = ('listing__title', )
    list_per_page = 100




admin.site.register(Listing , ListingAdmin)
admin.site.register(ListingPhoto , ListingPhotoAdmin)

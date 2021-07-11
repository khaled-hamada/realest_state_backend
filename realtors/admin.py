from django.contrib import admin
from .models import Realtor
# Register your models here.

## customize admin site view 
class RealtorAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'email', 'date_hired')
    list_display_links = ('id', 'name')
    list_filter = ('date_hired', 'top_seller', )
    search_fields = ('name','email', )
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Listing
from .serializers import ListingSerializer, ListingDetailSerializer
from datetime import datetime, timezone, timedelta
import re
from rest_framework.parsers import JSONParser
class ListingsView(ListAPIView):
    queryset = Listing.objects.filter(is_published = True).order_by('-list_date')
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    lookup_field = 'slug'


class ListingDetailView(RetrieveAPIView):
    queryset = Listing.objects.filter(is_published=True).order_by('-list_date')
    serializer_class = ListingDetailSerializer
    lookup_field = 'slug'



class SearchView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListingSerializer
    # parser_classes = [JSONParser]

    def post(self, request , format = None):
        data = request.data
        print(data)
        queryset = Listing.objects.filter( is_published=True).order_by('-list_date')
        
        sale_type = data['sale_type']
        queryset = queryset.filter(sale_type__iexact=sale_type)

        price = data['price']
        try:
            price = int(re.findall('\d+',price)[0])
        except:
            price = -1

        if price != -1:
            queryset = queryset.filter(price__gte=price)
        
        
        bedrooms = data['bedrooms']
        try:
            bedrooms = int(re.findall('\d+', bedrooms)[0])
        except:
            bedrooms =0
        

        queryset = queryset.filter(bedrooms__gte=bedrooms)

        home_type = data['home_type']
        queryset = queryset.filter(home_type__iexact=home_type)


        bathrooms = data['bathrooms']
        try:
            bathrooms = float(re.findall('\d+', bathrooms)[0])
        except:
            bathrooms = 0.0
        
        queryset = queryset.filter(bathrooms__gte=bathrooms)


        sqft = data['sqft']
        try:
            sqft = float(re.findall('\d+', sqft)[0])
        except:
            sqft = 0
      
        
        if sqft != 0:
            queryset = queryset.filter(sqft__gte=sqft)

        days_passed = data['days_listed']
        try:
            days_passed = int(re.findall('\d+', days_passed)[0])
        except:
            days_passed = 0
       

        for query in queryset:
            num_days = (datetime.now(timezone.utc) - query.list_date).days

            if days_passed != 0:
                if num_days > days_passed:
                    slug=query.slug
                    queryset = queryset.exclude(slug__iexact=slug)
 


        has_photos = data['has_photos']
        try:
            has_photos = int(re.findall('\d+', has_photos)[0])
        except:
            has_photos =1
      
        for query in queryset:
            count = query.getListingPhotosCount
            if count < has_photos:
                slug = query.slug
                queryset = queryset.exclude(slug__iexact=slug)

        open_house = str(data['open_house'])
        # print(f"open_house is {open_house}")
        # open_house = True if open_house == 'true' else  False
        queryset = queryset.filter(open_house__iexact = open_house)

        keywords = data['keywords']
        queryset = queryset.filter(description__icontains = keywords)

        serializer = ListingDetailSerializer(queryset, many=True)

        return Response(serializer.data)

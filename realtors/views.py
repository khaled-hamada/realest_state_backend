from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Realtor
from .serializers import RealtorSerialzer

class RealtorsListView(ListAPIView):
    permission_classes = (permissions.AllowAny, ) ## anyone can see about , no need to be authenticated 
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerialzer
    pagination_class = None  ## because by default any  list class is pagintated 



## view specific realtor data 
# in this view we need to be authenticated so we will not all any permissions 
class RealtorView(RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerialzer




class TopSellerView(ListAPIView):
    permission_classes = (permissions.AllowAny, ) ## anyone can see about , no need to be authenticated 
    queryset = Realtor.objects.filter(top_seller = True)
    serializer_class = RealtorSerialzer
    pagination_class = None  ## because by default any  list class is pagintated 





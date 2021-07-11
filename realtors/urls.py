from django.urls import path
from .views import TopSellerView , RealtorView ,RealtorsListView

urlpatterns = [
    path('', RealtorsListView.as_view(), name="all_realtors" ),
    path('<pk>', RealtorView.as_view(), name="realtor"),
    path('topseller/', TopSellerView.as_view(), name="top_seller"),
]

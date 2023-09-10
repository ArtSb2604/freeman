from django.urls import path
from index.views import IndexView, AdvertisementView, FairsView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("advertisement", AdvertisementView.as_view(), name="advertisement"),
    path("fairs", FairsView.as_view(), name="fairs"),
]
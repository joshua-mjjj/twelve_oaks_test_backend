from django.urls import include, path

from api.views import (
    GetResturantsData,
    GetResturantsDetailData
)

urlpatterns = [
    path("restaurants/", GetResturantsData, name="restaurants"),
    path("restaurants/<str:pk>", GetResturantsDetailData, name="restaurants-detail"),
]
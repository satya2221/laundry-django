from django.urls import path
from .views import LaundryOrderListView

urlpatterns = [
    path("", LaundryOrderListView.as_view(), name="laundry-order"),
]
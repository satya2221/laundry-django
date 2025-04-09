from django.urls import path
from .views import LaundryOrderListView, CreateLaundryOrder

urlpatterns = [
    path("", LaundryOrderListView.as_view(), name="laundry-order"),
    path("createOrder", CreateLaundryOrder.as_view(), name="create-order")
]
from django.urls import path
from .views import LaundryOrderListView, CreateLaundryOrder, UpdateLaundryOrder

urlpatterns = [
    path("", LaundryOrderListView.as_view(), name="laundry-order"),
    path("createOrder", CreateLaundryOrder.as_view(), name="create-order"),
    path("updateOrder/<str:pk>", UpdateLaundryOrder.as_view(), name="update-order")
]
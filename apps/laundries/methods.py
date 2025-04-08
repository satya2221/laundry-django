import time

from .models import LaundryItem, LaundryOrder
from apps.profiles.models import Profile


def process_laundry(customer, expected_date, quantity, price_per_quantity):
    print("Processing Laundry")

    print(f"Processing Laundry Order for  {order.customer.profile.name} ")

    order = LaundryOrder.objects.create(customer=customer, expected_date=expected_date)

    time.sleep(15)

    LaundryItem.objects.create(order=order, quantity=quantity, price_per_quantity=price_per_quantity)

    print(f"Finalizing Laundry order for {order.customer.profile.name} ")
    time.sleep(10)

    print(f"Laundry order {order.id} is successfully created!")

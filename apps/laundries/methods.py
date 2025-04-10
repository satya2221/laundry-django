import time
from datetime import datetime

from django.contrib.auth.models import User

from .models import LaundryItem, LaundryOrder
from apps.profiles.models import Profile, ProfileSetting


def process_laundry(customer, actor, expected_date, quantity, price_per_quantity):
    print("Processing Laundry")

    order = LaundryOrder.objects.create(
        customer=customer, 
        expected_completion_date=expected_date,
        actor = actor
        )
    print(f"Processing Laundry Order for  {order.customer.profile.name} ")

    time.sleep(5)

    LaundryItem.objects.create(order=order, 
                               quantity=quantity, 
                               price_per_quantity=price_per_quantity,
                               actor=actor
                               )

    print(f"Finalizing Laundry order for {order.customer.profile.name} ")
    time.sleep(2)

    print(f"Laundry order {order.id} is successfully created!")

def search_user_customer(cust_username, phone):
    user = User.objects.filter(username=cust_username).first()
    if user:
        return user
    else:
        timestamp = datetime.now().strftime("%d%m%y_%H%M")
        new_username = f"{cust_username}_{timestamp}"

        user = User.objects.create_user(
            username=new_username,
            password='defaultpassword123',  
        )

        ProfileSetting.objects.create(
            role="customer",
            actor = user
        )

        Profile.objects.create(
            actor= user,
            name = cust_username,
            phone = phone
        )
        return user
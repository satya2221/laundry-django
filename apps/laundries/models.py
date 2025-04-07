from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel
from apps.profiles.models import Profile

# Create your models here.
LAUNDRY_STATUS_CHOICES = (
    ('received', 'Received'),
    ('washing', 'Washing'),
    ('drying', 'Drying'),
    ('ironing', 'Ironing'),
    ('completed', 'Completed'),
)

class LaundryOrder(BaseModel):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    received_date = models.DateField(auto_now_add=True)
    expected_completion_date = models.DateField()
    status = models.CharField(max_length=20, choices=LAUNDRY_STATUS_CHOICES, default='received')

class LaundryItem(BaseModel):
    order = models.OneToOneField(LaundryOrder, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=8, decimal_places=2)
    price_per_quantity = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def total_price(self):
        return self.quantity * self.price_per_item
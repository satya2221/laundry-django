from huey.contrib.djhuey import task
from .methods import process_laundry

@task()
def task_process_laundry(customer, expected_date, quantity, price_per_quantity):
    process_laundry(customer, expected_date, quantity, price_per_quantity)
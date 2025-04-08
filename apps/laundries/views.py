from django.shortcuts import render, redirect
from django.views.generic import ListView, View

from core.views import LoginRequiredMixinView
from apps.profiles.models import ProfileSetting, Profile

from .models import LaundryOrder
from .tasks import task_process_laundry

# Create your views here.
class LaundryOrderListView(LoginRequiredMixinView, ListView):
    model = LaundryOrder
    template_name = "laundry_order.html"
    context_object_name = "laundries"

    def get_queryset(self):
        user_settings = ProfileSetting.objects.get(actor=self.request.user)
        if(user_settings.role == 'staff'):
            return LaundryOrder.objects.filter(actor=self.request.user)
        else:
            return LaundryOrder.objects.filter(customer=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.filter(actor=self.request.user).first()
        user_settings = ProfileSetting.objects.get(actor=self.request.user)

        context['profile'] = profile
        context['user_settings'] = user_settings

        return context

class CreateLaundryOrder(LoginRequiredMixinView, View):
    def get(self, request):
        user_settings = ProfileSetting.objects.get(actor=self.request.user)
        return render(request, 'create_laundry_order.html', {'user_settings': user_settings})
    
    def post(self, request):
        customer = request.POST.get('customer')
        expected_date = request.POST.get('completion_date')

        quantity = request.POST.get('quantity')
        price_per_quantity = request.POST.get('price')

        task_process_laundry(customer, expected_date, quantity, price_per_quantity)

        return redirect('laundry_order')
        
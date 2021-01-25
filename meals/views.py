from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Meals, Category
from .service import get_order_info


class MealsListView(ListView):
    """Вывод списка блюд"""

    model = Meals
    context_object_name = 'meals'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class OrderView(View):
    def post(self, request):
        data = request.POST
        context = get_order_info(data)
        return render(request, 'meals/order.html', context)

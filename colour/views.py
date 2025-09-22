from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import FoodForm
from .models import Food

def food_view(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "success.html")  # a thank you page
    else:
        form = FoodForm()
    return render(request, "food.html", {"form": form})

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

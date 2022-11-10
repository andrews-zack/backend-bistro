from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Category, Cuisine
from pprint import pprint as pront
from django.forms.models import model_to_dict

def get_menu(request):
    data = []
    menu = list(MenuItem.objects.all())
    for item in menu:
        data.append({
            'title': item.title,
            'price': '$'+str(item.price),
            'description': item.desc,
            'spicy': item.spicy,
            'category': model_to_dict(item.category_id),
            'cuisine': model_to_dict(item.cuisine_id)
        })
    return JsonResponse(data, safe=False)


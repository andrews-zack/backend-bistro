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
            'category': model_to_dict(item.category),
            'cuisine': model_to_dict(item.cuisine)
        })
    return JsonResponse(data, safe=False)

def menu_by_cuisine(request, cuisine):
    # data = []
    cuisine = list(MenuItem.objects.filter(cuisine__title=cuisine).values())
    # for item in cuisine:
    #     data.append({
    #         'title': item.title,
    #         'price': '$'+str(item.price),
    #         'description': item.desc,
    #         'spicy': item.spicy,
    #         'category': model_to_dict(item.category),
    #         'cuisine': model_to_dict(item.cuisine)
    #     })
    if len(cuisine) > 0:
        return JsonResponse(cuisine, safe=False)
    else:
        return HttpResponse("Sorry, we don't currenty have that food")

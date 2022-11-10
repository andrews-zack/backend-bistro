from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Category, Cuisine
from pprint import pprint as pront
from django.forms.models import model_to_dict

def get_menu(request):
    menu = list(MenuItem.objects.values())
    # for x in menu:
    #     model_to_dict(x)
    return JsonResponse({'data': menu})


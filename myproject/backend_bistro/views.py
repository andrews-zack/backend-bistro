from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint as pront

def get_menu(request):
    pront(dir(request))


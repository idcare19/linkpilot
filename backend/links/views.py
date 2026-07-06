from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def link_list(request):
    return JsonResponse({
        "message":"linkpoilot api is working fine", 
    })

from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Link
from .utils import generate_short_code
# Create your views here.


@csrf_exempt
def link_list(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        original_url = data.get('original_url')
        
        if not original_url:
            return JsonResponse({"success": False, "error":"original_url is required"}, status=400)
        
        link = Link.objects.create(original_url=original_url, short_code=generate_short_code())
        
        return JsonResponse({"success": True,"message":"link created successfully","id": link.id,"original_url": link.original_url,"link": link.short_code})
    return JsonResponse({
        "success": True,
        "message":"linkpoilot api is working fine", 
    })

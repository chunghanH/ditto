from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from gallery.src.gallery import Gallery

import json

gallery = Gallery()

@require_http_methods(['GET'])
def projects(request):
    result = gallery.getProject()
    return JsonResponse(result)

@require_http_methods(['GET'])
def media(request, *args, **kwargs):
    result = gallery.getMedia(kwargs['pk'])
    return JsonResponse(result)
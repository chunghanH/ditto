from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from gallery.models import Project, Media
from django.views.generic import TemplateView, FormView

import json

class ProjectView(TemplateView):
    template_name = 'project.html'

    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        return render(request, self.template_name, {'projects': projects})

@csrf_exempt
@require_http_methods(['POST'])
def get_media(request):
    value = json.loads(request.body)
    result = {}
    try:
        pk = value['id']
        medias = Media.objects.filter(project=pk).values()
        result['status'] = '200'
        result['data'] = list(medias)
    except:
        result['status'] = '500'
    return JsonResponse(result)
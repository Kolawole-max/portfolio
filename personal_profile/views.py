from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    content = Content.objects.all()
    return render(request, 'main.html', {
        'contents' : Content.objects.all(),
        'projects' : Project.objects.all()
    })
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import produto


# Create your views here.

def index(request):
    mprod=produto.objects.all().values()
    context={
        'mprod':mprod
    }
    template=loader.get_template("index.html")
    return HttpResponse(template.render(context,request))
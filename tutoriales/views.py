from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render, get_object_or_404
from .models import *
from django.template import RequestContext

# Create your views here.
def principal(request):
    tutoriales = Tutoriales.objects.all()
    return render(request, "principal.html", {'tutoriales':tutoriales,},context_instance=RequestContext(request))

def html(request):
    tutoriales = Tutoriales.objects.all()
    return render(request, "tutoriales.html" ,{'tutoriales':tutoriales,},context_instance=RequestContext(request))

def descargas(request):
    descargas = Descargas.objects.all()
    return render(request, "descargas.html" ,{'descargas':descargas,},context_instance=RequestContext(request))

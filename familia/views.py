from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from familia.models import Curso


def profesor(request):
    return render(request, 'familia/profesores.html')

def inicio(self):
    inicio = loader.get_template("familia/inicio.html")
    documento = inicio.render()
    return HttpResponse(documento)

def estudiante(request):
    return render(request, 'familia/estudiantes.html')

def curso(self):
    curso = Curso(titulo="Python")
    curso.save()
    documento = f"familia"
    return HttpResponse(documento)

def curso(request):
    return render(request, 'familia/profesores.html')
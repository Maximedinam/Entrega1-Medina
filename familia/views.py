from django.shortcuts import render
from .models import ModeloFamilia
#familiares = [
    #{'id': 1, 'nombre': 'Julio Javier', 'apellido': 'Medina', 'descripcion': 'Soltero y con hijos.', 'edad': 52, 'fdn': '1968-09-16', 'parentesco': 'Padre'},
    #{'id': 2, 'nombre': 'Vilma', 'apellido': 'Monteporcci', 'descripcion': 'Soltera. ', 'edad': 50, 'fdn': '1970-06-15', 'parentesco': 'Madre'},
    #{'id': 3, 'nombre': 'Julio Ezequiel', 'apellido': 'Medina', 'descripcion': 'Soltero. Buen estudiante.', 'edad': 25, 'fdn': '1996-12-21', 'parentesco': 'Hermano'}
#] 

# Create your views here.
def inicio(request):
    familiares = ModeloFamilia.objects.all()
    contexto = {'familiares': familiares}
    return render(request, 'familia/inicio.html', contexto)

def miembro_de_familia(request, pk):
    pariente = ModeloFamilia.objects.get(id=int(pk))
    contexto = {'pariente': pariente}
    return render(request, 'familia/familiar.html', contexto)
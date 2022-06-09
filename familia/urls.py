from django.urls import path
from familia.views import inicio
from familia.views import profesor
from familia.views import estudiante
from familia.views import curso


urlpatterns = [
    path('', inicio, name="Inicio" ),
    path('profesor/' ,profesor, name="Profesor"),
    path('estudiante/', estudiante, name="Estudiante"),
    path('curso/', curso, name="Curso"),

]
from django.urls import path

from App import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.curso, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario', views.curso, name="CursoFormulario"),
    path('profesorFormulario', views.profesores, name="ProfesorFormulario"),
    path('buscar/', views.buscar),
   
]


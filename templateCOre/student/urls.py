
from django.urls import path
from . import views


app_name = 'student'


urlpatterns = [
    path('', views.allStudent, name='all'),
    path('add/', views.addStudent, name='add'),
    path('edit/', views.editStudent, name='edit'),
]
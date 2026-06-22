from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.index, name='index'),
]

from django.urls import path
from . import views

# This 'app_name' allows you to use the namespace 'engineering:index'
app_name = 'engineering'

urlpatterns = [
    path('', views.index, name='index'), # Resolves to /engineering/
]

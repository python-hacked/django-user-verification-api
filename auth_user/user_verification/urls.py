from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_user, name='create_user')
    
]

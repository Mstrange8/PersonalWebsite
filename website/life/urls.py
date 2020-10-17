from django.urls import path
from . import views

app_name = 'life'

urlpatterns = [
    path('life/', views.life_view, name="life"),
]

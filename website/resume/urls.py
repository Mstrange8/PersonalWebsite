from django.urls import path
from . import views

app_name = 'resume'

urlpatterns = [
    path('resume/', views.resume_view, name="resume"),
]

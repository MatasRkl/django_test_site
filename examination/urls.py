from django.urls import path
from . import views

app_name = 'examination'

urlpatterns = [
    path("", views.index, name="index"),
]
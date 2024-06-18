from django.urls import path
from . import views

app_name = 'examination'

urlpatterns = [
    path("", views.index, name="index"),
    path('persons/', views.get_persons, name='persons'),
    path('persons/<int:person_id>/', views.get_person, name='person_detail'),
    path('persons/<int:person_id>/delete/', views.delete_person, name='delete_person'),
]

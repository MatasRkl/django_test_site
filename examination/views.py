from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic


from django.shortcuts import render
from django.http import  HttpResponse
from .models import *

def index(request):
    return HttpResponse("Cia yra examination")


def get_persons(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'examination/persons.html', context)


def get_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    context = {'person': person}
    return render(request, 'examination/person_detail.html', context)


def delete_person(request, person_id):
    person = get_object_or_404(Person, id=person_id)

    if request.method == 'POST':
        person.delete()
        return redirect('examination:persons')

    context = {'person': person}
    return render(request, 'examination/person_delete.html', context)



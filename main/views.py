from django.shortcuts import render
import main.views

from main.models import Person, Contact


def home(requests):
    persons = Person.objects.all()
    condext = {
        'persons': persons
    }

    return render(requests, 'main/home.html', condext)


def contact(requests):
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts
    }
    return render(requests, 'main/contact.html', context)
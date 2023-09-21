import datetime
from parsers import *

from django.shortcuts import render


# Create your views here.
def home(request):
    parsers = (hh, superjob, zarplata)

    vacancys = []
    for pars in parsers:
        job = pars()
        vacancys += job
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {'date': date, 'name': name}
    return render(request, 'learning_app/home.html', _context)

import datetime
from parsers import *

from django.shortcuts import render


# Create your views here.
def home(request):
    parsers = (hh, superjob, zarplata)

    vacancy = []
    for pars in parsers:
        job = pars()
        vacancy += job
    date = datetime.datetime.now().date()
    name = 'Dave'
    context = {'date': date, 'name': name, 'vacancy': vacancy}
    return render(request, 'learning_app/home.html', context)

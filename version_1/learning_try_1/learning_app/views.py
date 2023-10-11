import datetime
from .forms import *
from parsers import *
from .models import *

from django.shortcuts import render


# Create your views here.
def home(request):
    # print(request.GET)
    if request.method == 'POST':
        # print(request.POST)
        form = FindForm(request.POST)
        if form.is_valid():
            data_for_find = form.cleaned_data.get('vacancy_find')
            a = 1

            parsers = (hh, superjob, zarplata)
            vacancy = []
            for pars in parsers:
                job = pars(data_for_find)
                vacancy += job
            b = 2
            for vac in vacancy:
                v = Vacancy(**vac)
                v.save()
            date = datetime.datetime.now().date()
            name = 'Dave'
            context = {'date': date, 'name': name, 'vacancy': vacancy, 'form': form}
            return render(request, 'learning_app/home.html', context)

    form = FindForm()
    date = datetime.datetime.now().date()
    name = 'Dave'
    context = {'date': date, 'name': name, 'form': form}

    return render(request, 'learning_app/home.html', context)


def input_one(request):
    form = FindForm()
    print(request.POST.get('vacancy_find'))

    return render(request, 'learning_app/input_one.html', {'form': form})

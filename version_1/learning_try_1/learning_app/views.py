import datetime
from .forms import *
from parsers import *

from django.shortcuts import render


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = FindForm()
        if form.is_valid():
            data_for_find = form.cleaned_data.get('vacancy_find')

            parsers = (hh, superjob, zarplata)
            vacancy = []
            for pars in parsers:
                job = pars(data_for_find)
                vacancy += job
            date = datetime.datetime.now().date()
            name = 'Dave'
            context = {'date': date, 'name': name, 'vacancy': vacancy, 'form': form}
            return render(request, 'learning_app/home.html', context)

    else:
        form = FindForm()
        date = datetime.datetime.now().date()
        name = 'Dave'
        context = {'date': date, 'name': name,  'form': form}
    return render(request, 'learning_app/home.html', context)


def input_one(request):
    form = FindForm()
    print(request.POST.get('vacancy_find'))

    return render(request, 'learning_app/input_one.html', {'form': form})

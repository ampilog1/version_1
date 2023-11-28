import datetime
from .forms import *
from accounts.models import *
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
            if request.user.is_authenticated:
                current_user = DearUser.objects.get(username=request.user)
                data_for_find = form.cleaned_data.get('vacancy_find')

                parsers = (hh, superjob, zarplata)
                vacancy = []
                for pars in parsers:
                    job = pars(data_for_find)
                    vacancy += job

                for vac in vacancy:
                    v = Vacancy(**vac)
                    a = 1
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


def list_view(request):
    if request.method == 'POST':
        # print(request.POST)
        form = FindForm(request.POST)
        if form.is_valid():

            data_for_find = form.cleaned_data.get('vacancy_find')

            parsers = (hh, superjob, zarplata)
            vacancy = []
            for pars in parsers:
                job = pars(data_for_find)
                vacancy += job
            for vac in vacancy:
                v = Vacancy(**vac)
                v.save()
            date = datetime.datetime.now().date()
            name = 'Dave'
            context = {'date': date, 'name': name, 'vacancy': vacancy}
            return render(request, 'learning_app/list.html', context)



def input_one(request):
    form = FindForm()
    print(request.POST.get('vacancy_find'))

    return render(request, 'learning_app/input_one.html', {'form': form})

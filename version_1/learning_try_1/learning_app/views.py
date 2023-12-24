import datetime
from .forms import *
from accounts.models import *
from parsers import *
from .models import *

from django.shortcuts import render


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = FindForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                data_for_find = form.cleaned_data.get('vacancy_find')

                parsers = (hh, superjob, zarplata)
                vacancy = []
                for pars in parsers:
                    job = pars(data_for_find)
                    vacancy += job

                for vac in vacancy:
                    v = Vacancy()
                    v.name = vac['name']
                    v.link = vac['link']
                    v.address = vac['address']
                    v.salary = vac['salary']
                    v.owner = request.user
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
        form = FindForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                data_for_find = form.cleaned_data.get('vacancy_find')

                parsers = (hh, superjob, zarplata)
                vacancy = []
                for pars in parsers:
                    job = pars(data_for_find)
                    vacancy += job

                for vac in vacancy:
                    v = Vacancy()
                    v.name = vac['name']
                    v.link = vac['link']
                    v.address = vac['address']
                    v.salary = vac['salary']
                    v.owner = request.user
                    v.save()
            date = datetime.datetime.now().date()
            name = 'Dave'
            context = {'date': date, 'name': name, 'vacancy': vacancy, 'form': form}
            return render(request, 'learning_app/home.html', context)


def input_one(request):
    form = FindForm()
    print(request.POST.get('vacancy_find'))

    return render(request, 'learning_app/input_one.html', {'form': form})


def delete_old(request):
    two_days_ago = datetime.date.today() - datetime.timedelta(10)
    Vacancy.objects.filter(data_added__lte=two_days_ago).delete()
    return render(request, 'learning_app/home.html', 'delete')

import datetime

from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, \
    DeleteView

from .forms import FindForm, VForm
from .models import Vacancy



# Create your views here.
def home(request):
    date = datetime.datetime.now().date()
    name = 'Dave'
    _context = {'date': date, 'name': name}
    return render(request, 'home.html', _context)
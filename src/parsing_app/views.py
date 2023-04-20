from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, \
    DeleteView

from .forms import FindForm, VForm
from .models import Vacancy


def home_view(request):
    # print(request.GET)
    form = FindForm()

    return render(request, 'scraping/home.html', {'form': form})

# Create your views here.

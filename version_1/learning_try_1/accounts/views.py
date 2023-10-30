from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import *
from django.urls import reverse_lazy

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


class UserCreateView(CreateView):
    model = DearUser
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')


from django.shortcuts import render

# Create your views here.

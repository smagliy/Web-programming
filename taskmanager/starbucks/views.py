from django.shortcuts import render, redirect
from .forms import RegistrationForm


def index(request):
    return render(request, 'starbucks/index.html')


def registration(request):
    err = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            err = 'Не правильно введенна форма'
    form = RegistrationForm()
    data = {
        'form': form,
        'err': err
    }
    return render(request, 'starbucks/registration.html', data)
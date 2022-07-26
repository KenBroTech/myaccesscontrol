from django.shortcuts import redirect, render
from .forms import CaesarEncryptForm, AESEncryptForm, cautionModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')


def caesar(request):
    if request.method == 'POST':
        form = CaesarEncryptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = CaesarEncryptForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/caesar.html', context)


def aes(request):
    if request.method == 'POST':
        form = AESEncryptForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index')
    else:
        form = AESEncryptForm()
    context = {
        'form':form
    }
    return render(request, 'dashboard/aes.html', context)


def caution(request):
    if request.method == 'GET':
        form = cautionModelForm(request.GET)
        if form.is_valid():
            form.save()
    else:
        form = cautionModelForm()
    context = {
        'form':form
    }
    return render(request, 'dashboard/caution.html', context)

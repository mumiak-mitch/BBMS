from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import DocRegForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def docreg(request):
    if request.method == "POST":
        form = DocRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, your account has been created successfully.')
            return redirect('doclog')
    else:
        form = DocRegForm
        
    return render(request, 'home/docreg.html', {'form':form})

@login_required
def dochome(request):
    return render(request, 'home/dochome.html')

@login_required
def docprof(request):
    return render(request, 'home/docprof.html')
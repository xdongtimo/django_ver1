from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
import ctypes

def index(request):
    return render(request, 'pages/home.html')
# Create your views here.
def contact(request):
    return render(request, 'pages/contact.html')

def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})

# Create function register to controller
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            ctypes.windll.user32.MessageBoxW(0, "Register success !!!", "Status", 0)
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html',{'form': form})
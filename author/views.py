from django.shortcuts import render

from .forms import RegisterForm

# Create your views here.
def register(request):

    form = RegisterForm()
    return render(request, 'author/pages/register.html', {
        'form':form
        }
    )
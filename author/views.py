from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.http import Http404
from django.contrib import messages

# Create your views here.
def register(request):

    register_form_data = request.session.get('register_form_data', None)

    form = RegisterForm(register_form_data)

    return render(request, 'author/pages/register.html', {
        'form':form
        }
    )


def register_create(request):
    if not request.POST:
        raise Http404('Only POSTs are allowed')

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)


    if form.is_valid():
        form.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')

        del(request.session['register_form_data'])

    return redirect('authors:register')
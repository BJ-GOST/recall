from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth, messages
from .forms import signUpForm

# Create your views here.
def index(request):
    template_name = 'index.html'
    return render(request, template_name)


def logIn(request):
    template_name = 'login.html'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user = request.user
            return redirect('home')
        else:
            messages.error(request, 'Check password or username')
    return render(request, template_name, context={'messages':messages})



def signUp(request):
    form = signUpForm()
    template_name = 'signup.html'
    context = {
        'form':form
    }
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, template_name, context)


def logOut(request):
    auth.logout(request)
    return redirect('index')
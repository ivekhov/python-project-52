from django.shortcuts import render

def index(request):
    return render(request, 'index.html', context={
        'who': 'World',
    })


def users(request):
    return render(request, 'users.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


def sign_up_by_html(request):
    users = ['Dan', 'Anton']
    info = {}
    context = {
        "info": info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password == repeat_password and age >= 18 and username not in users:
            return HttpResponse(f'Приветсвуем, {username}!')
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        if age < 18:
            info['error'] = 'Вы должны быть старше 18'
        if username in users:
            info['error'] = 'Пользователь уже существует'

    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = ['Dan', 'Anton']
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])


            if password == repeat_password and age >= 18 and username not in users:
                return HttpResponse(f'Приветсвуем, {username}!')
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            if age < 18:
                info['error'] = 'Вы должны быть старше 18'
            if username in users:
                info['error'] = 'Пользователь уже существует'
    else:
        form = UserRegister()

    return render(request, 'registration_page.html', {'form': form, "info": info})

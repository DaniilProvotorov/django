from django.shortcuts import render


def home(request):
    return render(request, 'homepage.html')


def cats(request):
    p1 = "Сиамская кошка"
    p2 = "Сфинкс"
    p3 = "Бурма"
    context = {"p1": p1,
               "p2": p2,
               "p3": p3,
               }
    return render(request, 'cats.html', context)


def func(request):
    f1 = "Записаться на посещение"
    f2 = "Внести пожертвование"
    f3 = "Приручить питомца"
    context = {
        "f1": f1,
        "f2": f2,
        "f3": f3,
    }
    return render(request, 'func.html', context)


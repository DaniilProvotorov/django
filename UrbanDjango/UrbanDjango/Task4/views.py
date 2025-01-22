from django.shortcuts import render


def home(request):
    return render(request, 'homepage.html')


def cats(request):
    p1 = "Сиамская кошка"
    p2 = "Сфинкс"
    p3 = "Бурма"
    list_p = [p1, p2, p3]
    context = {"p1": p1,
               "p2": p2,
               "p3": p3,
               "list_p": list_p
               }
    return render(request, 'cats.html', context)


def func(request):
    list_f = ["Записаться на посещение", "Внести пожертвование", "Приручить питомца"]
    context = {
        "list_f": list_f,
    }
    return render(request, 'func.html', context)
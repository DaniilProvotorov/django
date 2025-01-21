from django.shortcuts import render

# Create your views here.


def cl(request):
    return render(request, 'class.html')


def fu(request):
    return render(request, 'func.html')

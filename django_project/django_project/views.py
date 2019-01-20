from django.shortcuts import render


def home(request):
    return render(request, 'minerals/list.html')


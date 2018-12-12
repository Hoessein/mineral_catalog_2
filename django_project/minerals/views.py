from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect

import json

import random


from .models import Mineral


def home(request):
    minerals = Mineral.objects.filter()
    return render(request, 'minerals/index.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = Mineral.objects.filter(pk=pk)

    with open('minerals.json', encoding='utf8') as file:
        data = json.load(file)

    return render(request, 'minerals/detail.html', {'mineral': mineral, 'data': data})


def random_mineral(request):
    """"Gives back a random object."""
    random_mineral = Mineral.objects.order_by('?').first().pk
    return HttpResponseRedirect(reverse('minerals:mineral_detail', args=(random_mineral,)))


if __name__ == '__main__':
    Mineral.json_to_db()

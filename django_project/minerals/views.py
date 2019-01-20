from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q

from .models import Mineral

from . import forms


def home(request):
    """Will show all the minerals on the homepage
    renders list.html and stores all the objects to 'mineral' """
    minerals = Mineral.objects.filter(name__istartswith='a')
    return render(request,
                  'minerals/list.html',
                  {'minerals': minerals}
                  )


def mineral_detail(request, pk):
    """Will show each mineral on a separate detail page
    if the object doesn't exists it will throw a 404 error"""
    mineral = Mineral.objects.filter(pk=pk)
    if mineral.exists():
        return render(request, 'minerals/detail.html', {'mineral': mineral})
    else:
        raise Http404


def random_mineral(request):
    """"Gives back a random object"""
    random_mineral = Mineral.objects.order_by('?').first().pk
    return HttpResponseRedirect(reverse('minerals:mineral_detail', args=(random_mineral,)))


def alphabet(request, letter):
    """something"""
    minerals = Mineral.objects.filter(name__istartswith=letter)
    return render(request, 'minerals/list.html', {'minerals': minerals})


def search_mineral(request):
    query = request.GET.get('q')
    minerals = Mineral.objects.filter(name__icontains=query)
    return render(request, 'minerals/list.html', {'minerals': minerals})


def group_mineral(request, group_name):
    minerals = Mineral.objects.filter(group__icontains=group_name)
    return render(request, 'minerals/list.html', {'minerals': minerals})






from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q

from .models import Mineral

from . import forms


def home(request):
    """Will show all the minerals on the homepage
    renders index.html and stores all the objects to 'mineral' """
    default_homepage_mineral = Mineral.objects.filter(name__istartswith='a')
    return render(request,
                  'minerals/index.html',
                  {'default_homepage_mineral': default_homepage_mineral}
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
    mineral_by_letter = Mineral.objects.filter(name__istartswith=letter)
    return render(request, 'minerals/minerals_by_letter.html', {'mineral_by_letter': mineral_by_letter})


def search_mineral(request):
    query = request.GET.get('q')
    results = Mineral.objects.filter(name__icontains=query)
    return render(request, 'minerals/minerals_by_search.html', {'results': results, 'form': form})


# def group_mineral(request):
#     groups = Mineral.objects.filter('g)
#
#



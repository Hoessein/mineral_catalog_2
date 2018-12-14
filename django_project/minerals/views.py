from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, Http404


from .models import Mineral


def home(request):
    """Will show all the minerals on the homepage
    renders index.html and stores all the objects to 'mineral' """
    minerals = Mineral.objects.filter()
    return render(request, 'minerals/index.html', {'minerals': minerals})


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

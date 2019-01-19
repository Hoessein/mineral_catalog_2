from . import forms
from .models import Mineral

def alphabet_grid(request):
    """something"""
    alphabet = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
    return {'alphabet': alphabet}


def search(request):
    form = forms.SearchForm()
    return {'form': form}


def group(request):
    groups = Mineral.objects.order_by().values('group').distinct()
    # hondje = []
    # for x in groups:
    #     hondje.append(x)
    # groupa = set(hondje)
    return {'groups': groups}

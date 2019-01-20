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
    group_list = []
    for x in groups:
        group_list.append(x)
    return {'group_list': group_list}

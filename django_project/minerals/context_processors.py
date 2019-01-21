from . import forms
from .models import Mineral

def alphabet_grid(request):
    """A list of alphabet letters that will be showed in the layout"""
    alphabet = [letter for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
    return {'alphabet': alphabet}


def search(request):
    """An instance of form so that the search field can be showed in the layout"""
    form = forms.SearchForm()
    return {'form': form}


def group(request):
    """SHows each group value of the minerals."""
    groups = Mineral.objects.order_by().values('group').distinct()
    group_list = []
    for x in groups:
        group_list.append(x)
    return {'group_list': group_list}

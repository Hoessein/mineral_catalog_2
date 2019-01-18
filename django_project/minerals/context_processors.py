from . import forms


def alphabet_grid(request):
    """something"""
    alphabet = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
    return {'alphabet': alphabet}


def search(request):
    form = forms.SearchForm()
    return {'form': form}




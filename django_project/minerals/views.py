from django.shortcuts import render, get_object_or_404


from .models import Mineral

def home(request):
    minerals = Mineral.objects.filter()
    return render(request, 'minerals/index.html', {'minerals': minerals})

def mineral_detail(request, pk):
    mineral = Mineral.objects.filter(pk=pk)
    return render(request, 'minerals/detail.html', {'mineral': mineral})


if __name__ == '__main__':
    Mineral.json_to_db()

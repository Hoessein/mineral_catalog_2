from django.shortcuts import render, get_object_or_404


from .models import Mineral

def home(request):
    minerals = Mineral.objects.filter()
    return render(request, 'minerals/index.html', {'minerals': minerals})

def mineral_detail(request, pk):
    mineral = Mineral.objects.filter(pk=pk)

    # d = {}
    # for x in Mineral._meta.get_fields():
    #     # if x.name != 'id' or 'name' or 'image_filename':
    #     d[x.name] = getattr(Mineral, x.name)
    #     # else:
    #     #     pass

    return render(request, 'minerals/detail.html', {'mineral': mineral,
                                                    'd': d})


if __name__ == '__main__':
    Mineral.json_to_db()

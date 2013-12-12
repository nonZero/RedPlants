from django.shortcuts import render, get_object_or_404
from plants.models import Specie


def specie_list(request):
    l = Specie.objects.all()
    return render(request, "plants/specie_list.html", {'object_list': l})


def specie(request, pk):
    o = get_object_or_404(Specie, pk=int(pk))
    return render(request, "plants/specie_detail.html", {'object': o})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from plants.models import Specie, UserSpecie
from django.http.response import HttpResponseNotAllowed


def specie_list(request):
    l = Specie.objects.all()
    return render(request, "plants/specie_list.html", {'object_list': l})


@login_required
def specie(request, pk):
    o = get_object_or_404(Specie, pk=int(pk))
    return render(request, "plants/specie_detail.html", {
                         'object': o,
                         'user_like': o.users.filter(user=request.user).count(),
                         'likes': o.users.count()
                         })


@login_required
def like_specie(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed("Must be POST")
    o = get_object_or_404(Specie, pk=int(pk))
    UserSpecie.objects.get_or_create(user=request.user, specie=o)
    return redirect(o)


@login_required
def unlike_specie(request, pk):
    if request.method != "POST":
        return HttpResponseNotAllowed("Must be POST")
    o = get_object_or_404(Specie, pk=int(pk))
    UserSpecie.objects.filter(user=request.user, specie=o).delete()
    return redirect(o)

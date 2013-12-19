from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from obs import models


class CreateObservationView(CreateView):
    model = models.Observation
    success_url = reverse_lazy('obs')


class ObservationListView(ListView):
    model = models.Observation

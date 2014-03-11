__author__ = 'Lukasz'

from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy

from .models import Pensioner
from .forms import ReadOnlyPensionerModelForm, ReadWritePensionerModelForm

class PensionerListView(generic.ListView):
    model = Pensioner

class PensionerDetailView(generic.DetailView):
    model = Pensioner

class PensionerDetailViewForm(generic.UpdateView):
    model = Pensioner
    form_class = ReadOnlyPensionerModelForm

class PensionerUpdateViewForm(generic.UpdateView):
    model = Pensioner
    form_class = ReadWritePensionerModelForm
    success_url=reverse_lazy('cbv_list')

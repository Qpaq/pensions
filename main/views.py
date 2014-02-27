# Create your views here.
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

from .models import Pensioner
from .forms import ReadOnlyPensionerModelForm, ReadWritePensionerModelForm

def home(request):
    pensioner = Pensioner.objects.filter(surname="Smith")[0]
    return render(request, 'index.html', {'pensioner': pensioner})

def index(request):
    list = Pensioner.objects.all().order_by('-surname')[:5] #  List 5 members
    return render(request, 'list.html', {'list': list})

def detail(request, reference):
    pensioner = Pensioner.objects.filter(reference=reference)[0]
    return render(request, 'detail.html', {'pensioner': pensioner})

def edit(request, reference):
    pensioner = Pensioner.objects.filter(reference=reference)[0]

    if request.method == 'POST':
        pensioner.title = request.POST['title']
        pensioner.forename = request.POST['forename']
        pensioner.surname = request.POST['surname']
        pensioner.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('main.views.home'))

    return render(request, 'detail_edit.html', {'pensioner': pensioner})

def detail_form(request, reference):
    pensioner = Pensioner.objects.filter(reference=reference)[0]
    form = ReadOnlyPensionerModelForm(instance=pensioner)
    return render(request, 'detail_form.html', {'form': form, 'pensioner': pensioner})

def edit_form(request, reference):
    pensioner = Pensioner.objects.filter(reference=reference)[0]
    if request.method == 'POST':
        form = ReadWritePensionerModelForm(request.POST, instance=pensioner)
        if form.is_valid(): 			# If not validated then field exception
            form.save(reference=reference)
        return HttpResponseRedirect(reverse('main.views.detail_form', args=(pensioner.reference,)))
    else:
        form = ReadWritePensionerModelForm(instance=pensioner)
    return render(request, 'detail_edit_form.html', {'form': form, 'pensioner':pensioner})

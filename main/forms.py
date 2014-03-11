__author__ = 'Lukasz'


from django.forms import ModelForm, TextInput, ChoiceField
from django.forms.widgets import Textarea, HiddenInput, Select
from .models import Pensioner

class BasePensionerModelForm(ModelForm):
    class Meta:
        model = Pensioner

class ReadOnlyPensionerModelForm(BasePensionerModelForm):
    class Meta(BasePensionerModelForm.Meta):
        fields = ['title', 'forename', 'surname']
        widgets = {
            'title': TextInput(attrs={'readonly':'readonly'}),
            'forename': TextInput(attrs={'readonly':'readonly'}),
            'surname': TextInput(attrs={'readonly':'readonly'}),
        }

class ReadWritePensionerModelForm(BasePensionerModelForm):

    def save(self, commit=True):
        Pensioner.objects.filter(reference=self.cleaned_data['reference']).update(
            title=self.cleaned_data['title'],
            forename=self.cleaned_data['forename'],
            surname=self.cleaned_data['surname'])
        # commit=False means the form doesn't save at this time.
        return super(ReadWritePensionerModelForm, self).save(commit=False)


    class Meta(BasePensionerModelForm.Meta):
        fields = ['reference', 'title', 'forename', 'surname']
        labels = {'reference': 'Reference Number',}
        widgets = {
            'reference': TextInput(attrs={'readonly':'readonly'}),  # reference is read only
        }
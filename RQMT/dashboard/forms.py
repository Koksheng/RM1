from django import forms
from dashboard.models import *
from django_select2.forms import Select2MultipleWidget


class ModuleRequirementForm(forms.ModelForm):
    # machine_rqmt = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    # machine_rqmt = forms.ModelMultipleChoiceField(queryset=MachineRequirement.objects.none())

    class Meta:
        model = ModuleRequirement
        fields = ['title','machine_rqmt']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please insert a title', 'autocomplete':'off'}),
            # 'machine_rqmt': forms.CheckboxSelectMultiple(),
            # 'machine_rqmt': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Please insert a title', 'autocomplete':'off'}),
            'machine_rqmt': Select2MultipleWidget(),
            # 'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please select a burn in process stage', 'autocomplete':'off'}),
        }
        labels = {
            'title': ('Title'),
            'machine_rqmt': ('Machine Requirement'),
            # 'availability': ('Availability'),
        }
        error_messages = {
        }

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['machine_rqmt'].queryset = MachineRequirement.objects.all()
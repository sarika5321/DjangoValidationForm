from django import forms
from app.models import *

def validator_for_b(data):
    fdata = data.lower()
    if fdata.startswith('b'):
        raise forms.validationError('The School Name is startting with "B"')

def validator_for_len(data):
    if len(data)>5:
        raise forms.ValidationError('Has More than 5 characters')  
    
def validation_for_duplicate(data):
    SO = school.objects.get(sname=data)
    if SO:
        raise forms.ValidationError('school already exits')
    
class schoolForm(forms.Form):
    sname = forms.CharField(max_length=50, required=False, validators=[validator_for_b,validator_for_len])
    sprincipal = forms.CharField( max_length=50, required=False)
    saddress = forms.CharField( max_length=50, required=False)
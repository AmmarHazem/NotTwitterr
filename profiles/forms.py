from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    name = forms.CharField(max_length = 50, widget = forms.TextInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Full Name'}), required = False)
    
    birth_date = forms.DateField(widget = forms.DateInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'YYYY-MM-DD'}), required = False)
    
    bio = forms.CharField(widget = forms.Textarea(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Descripe your self'}), required = False)
    
    location = forms.CharField(max_length = 20, widget = forms.TextInput(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'Location'}), required = False)

    avatar = forms.ImageField(required = False, label = 'Choose an Avatar', widget = forms.FileInput(attrs = {'class': 'inputfile', 'data-multiple-caption' : '{count} files selected'}))

    cover = forms.ImageField(label = 'Choose a Cover', required = False, widget = forms.FileInput(attrs = {'class': 'inputfile', 'data-multiple-caption' : '{count} files selected'}))

    class Meta:
        model = Profile
        fields = ('bio', 'avatar', 'cover', 'birth_date', 'location')
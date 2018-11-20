from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):

    text = forms.CharField(label = '', widget = forms.Textarea(attrs = {'class' : 'form-control form-control-sm', 'placeholder' : 'What\'s happening ?', 'rows' : '2'}), required = False)
    image = forms.ImageField(label = 'Upload an Image', required = False, widget = forms.FileInput(attrs = {'class': 'inputfile', 'data-multiple-caption' : '{count} files selected'}))

    def clean(self):
        cd = super(TweetForm, self).clean()
        if not cd['text'] and not cd['image']:
            raise forms.ValidationError('Please enter a tweet text or an image.', code = 'invalid')

    class Meta:
        model = Tweet
        fields = ('text', 'image')
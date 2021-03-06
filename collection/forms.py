from django import forms
from django.forms import ModelForm

from collection.models import Thing


class ThingForm(ModelForm):
    class Meta:
        model = Thing
        fields = ('name', 'description',)


# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField()
    contact_email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:" 
        self.fields['contact_email'].label = "Your email:" 
        self.fields['content'].label = "What do you want to say?"
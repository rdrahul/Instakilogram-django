"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from models import Item,Photo
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description')
    def __init__(self,*args,**kwargs):
        super(AlbumForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_class='form-horizontal'
        self.helper.label_class='col-md-offset-1 col-md-2'
        self.helper.field_class='col-md-6'
        self.helper.add_input(Submit('submit','Create'))

class PhotoForm(forms.ModelForm):
    class Meta:
        model=Photo
        fields=('title','caption','image','caption')
    def __init__(self,*args,**kwargs):
        super(PhotoForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_class='form-horizontal'
        self.helper.label_class='col-md-offset-1 col-md-2'
        self.helper.field_class='col-md-6'
        self.helper.add_input(Submit('submit','Create'))
    
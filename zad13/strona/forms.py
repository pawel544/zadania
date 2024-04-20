from django.forms import ModelForm, CharField, TextInput
from .models import Author, Quate



class AuthorForms(ModelForm):
    name=CharField(min_length=2, max_length=30, required=True, widget=TextInput())

    class Meta:
        model=Author
        fields=['name']
class QuateForms(ModelForm):
    form_quate= CharField(min_length=5, max_length=100, required=True, widget=TextInput())

    class Meta:
        model=Quate
        fields=['form_quate']
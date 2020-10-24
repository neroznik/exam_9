from django import forms
from webapp.models import Picture

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = ['author', 'uploaded', 'fav_picture']





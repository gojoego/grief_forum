from django import forms 
from .models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['poster_name', 'deceased_name', 'background_story', 'message_to_deceased']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True 
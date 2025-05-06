from django import forms 
from .models import Post 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['deceased_name', 'background_story', 'message_to_deceased']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True 
            
class CustomUserCreationForm(UserCreationForm):
    display_name = forms.CharField(max_length=30, required=True, label='your name (as poster)')
    email = forms.EmailField(required=True, help_text="required - please enter a valid email address")
    
    class Meta:
        model = User 
        fields = ("username", "display_name", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["display_name"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
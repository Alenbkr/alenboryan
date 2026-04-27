from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'user_name', 'user_email', 'message']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Тема сообщения'}),
            'user_name': forms.TextInput(attrs={'placeholder': 'Ваше имя'}),
            'user_email': forms.EmailInput(attrs={'placeholder': 'Ваш email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Сообщение', 'rows':5}),
        }

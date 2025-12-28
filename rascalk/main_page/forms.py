from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('user', 'rating', 'text',)  # Теперь показываем все поля
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),  # Простое текстовое поле для имени пользователя
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})

        }




class VoteForm(forms.Form):
    CHOICES = [
        ('screenshot1', 'Screenshot 1'),
        ('screenshot2', 'Screenshot 2')
    ]
    vote_option = forms.ChoiceField(widget=forms.RadioSelect(), choices=CHOICES)
from django import forms
from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Task Title'}),
            "description": forms.Textarea(attrs={'cols':40, 'rows':10, 'class': 'form-control', 'placeholder': 'Enter Task Description'}),
            "due_date": forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


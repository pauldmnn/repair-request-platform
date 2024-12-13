from django import forms
from.models import RepairRequest


class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['name', 'email', 'phone', 'location', 'category', 'description' ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
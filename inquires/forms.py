from django import forms
from inquires.models import Inquiry


class InquiryForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=Inquiry.GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
    )

    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'gender', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Please write your message here',
                'rows': 4,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        if len(phone) < 10:
            raise forms.ValidationError("Phone number must be at least 10 digits long.")
        return phone
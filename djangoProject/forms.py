from django.forms import ModelForm
from django import forms
from pkg_resources import require

from events.models import MedicalHistory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name','last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class MedicalHistoryForm (ModelForm):
    user_id = forms.HiddenInput
    is_chronic_disease = forms.RadioSelect()
    disease_type = forms.Select()
    is_on_medication = forms.RadioSelect()
    medication_name = forms.Textarea()
    is_allergic = forms.RadioSelect()
    allergy = forms.Textarea()

    class Meta:
        model = MedicalHistory
        fields = '__all__'
        widgets = {
            'is_chronic_disease': forms.RadioSelect(),
            'is_allergic': forms.RadioSelect(),
            'is_on_medication': forms.RadioSelect(),
        }
    def __init__(self, *args, **kwargs):
        super(MedicalHistoryForm, self).__init__(*args, **kwargs)
        # Set fields to not required
        self.fields['disease_type'].required = False
        self.fields['medication_name'].required = False
        self.fields['allergy'].required = False



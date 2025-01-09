from django import forms

from Workshop.core.form_mixin import DisabledFormMixin
from Workshop.pets.models import Pet


class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name', 'date_of_birth', 'personal_photo')
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'personal_photo': forms.URLInput(attrs={'placeholder': 'Link to image'}),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):
    pass


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        else:
            pass
        return self.instance

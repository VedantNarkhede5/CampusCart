from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'college_name',
            'department',
            'year',
            'phone',
            'upi_id',
            'bio',
            'profile_photo'
        ]
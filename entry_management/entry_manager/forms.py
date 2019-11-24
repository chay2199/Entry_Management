from .models import CheckIn
from django import forms


class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = ['visitor_name', 'visitor_email', 'visitor_phone',
                  'host_name', 'host_email', 'host_phone']

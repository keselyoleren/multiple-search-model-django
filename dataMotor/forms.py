from django import forms
from  . models import Motor

class FormMotor(forms.ModelForm):
    class Meta:
        model = Motor
        fields = ('nama', 'thn_produksi', 'cc_motor')
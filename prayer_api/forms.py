from django import forms

class SelectCityForm(forms.Form):
    city = forms.ChoiceField(help_text='Select City', choices=[('ja', 'Jeddah'), ('ma', 'Makkah')])
from django import forms

class SelectCityForm(forms.Form):
    city = forms.ChoiceField(initial='ma' ,widget=forms.RadioSelect ,help_text='Select City', choices=[
        (
        'SA', (
            ('ja', 'Jeddah'),
            ('ma', 'Makkah')
            )
        )
    ]
)
from django import forms


CITES = [
    ('ma', 'Makkah'),
    ('me', 'Medina'),
    ('ri', 'Riyadh'),
    ('ja', 'Jeddah'),
    ('da', 'Dammam'),
    ('ta', 'Taif'),
    ('ab', 'Abha'),
    ('tb', 'Tabuk'),
    ('jz', 'Jazan'),
    ('ha', 'Hail'),
]

class SelectCityForm(forms.Form):
    city = forms.ChoiceField(initial='ma', widget=forms.RadioSelect, help_text='Select City', choices=[
        ('Saudi Arabia', (CITES))
    ])

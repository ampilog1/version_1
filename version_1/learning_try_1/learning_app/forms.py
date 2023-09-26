from django import forms


class FindForm(forms.Form):
    vacancy = forms.CharField(label='Вакансия', max_length=100)

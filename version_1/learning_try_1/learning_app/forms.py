from django import forms


class FindForm(forms.Form):
    vacancy = forms.CharField(label='��������', max_length=100)

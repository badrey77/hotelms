from django.forms import Form, SelectDateWidget, DateField, ModelForm, formset_factory
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import Input, DateInput, SelectDateWidget

from hebergement.models import Chambre


class CalendarForm(Form):
    picker = DateField(widget=AdminDateWidget())


class WelcomeForm(ModelForm):
    class Meta:
        model = Chambre
        fields = '__all__'


WelcomeFormSet = formset_factory(WelcomeForm)
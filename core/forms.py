import os.path

from django.forms import Form, SelectDateWidget, DateField, ModelForm, formset_factory, CharField
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import Input, DateInput, SelectDateWidget

from core.custom_widget import CustomLabelWidget
from hebergement.models import Chambre
from hotelms.settings import BASE_DIR


class CalendarForm(Form):
    picker = DateField(widget=AdminDateWidget())


class WelcomeForm(Form):
    content = CharField(widget=CustomLabelWidget(label_text='', source='/static/img/dessin5.png',attrs={}))

    def __init__(self, data, source, *args, **kwargs):
        super(WelcomeForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget = CustomLabelWidget(label_text=data, source=f'/static/img/{source}',attrs={})
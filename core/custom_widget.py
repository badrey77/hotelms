from django import forms
from django.forms.utils import flatatt
from django.template.loader import render_to_string


class CustomLabelWidget(forms.widgets.Widget):
    template_name = 'core/custom_label_widget_template.html'
    def __init__(self, label_text, source,attrs=None):
        super().__init__(attrs)
        self.label_text = label_text
        self.source = source

    def render(self, name, value, attrs=None, renderer=None):
        # Customize how the label widget is rendered in HTML
        attrs = self.build_attrs(attrs, {'src':self.source})
        context = {
            'attrs': flatatt(attrs),
            'label_title': name,
            'label_text': self.label_text,
            'name': name,
            'value': value,
        }
        rendered_template = render_to_string(self.template_name, context)
        return rendered_template

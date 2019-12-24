from django.db import models
from core.models import CoreModel
from bootstrap4.widgets import RadioSelectButtonGroup
from django import forms

# Create your models here.
class BasicDemo(CoreModel):
    name = models.CharField(max_length=512, verbose_name='测试字段')

class MyForm(forms.Form):
    media_type = forms.ChoiceField(
        help_text="Select the order type.",
        required=True,
        label="Order Type:",
        widget=RadioSelectButtonGroup,
        choices=((1, 'Vinyl'), (2, 'Compact Disc')),
        initial=1,
    )
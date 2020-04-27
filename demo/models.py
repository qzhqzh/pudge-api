from django.db import models
from core.models import CoreModel
from bootstrap4.widgets import RadioSelectButtonGroup
from django import forms


class Test(CoreModel):
    name = models.CharField(max_length=512, verbose_name='测试字段')


class BasicDemo(CoreModel):
    name = models.CharField(max_length=512, verbose_name='测试字段')
    test = models.BooleanField(default=False)
    test_fk = models.ForeignKey(Test, related_name='basicdemo', on_delete=models.CASCADE, verbose_name='测试用')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        return super(BasicDemo, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)

class MyForm(forms.Form):
    media_type = forms.ChoiceField(
        help_text="Select the order type.",
        required=True,
        label="Order Type:",
        widget=RadioSelectButtonGroup,
        choices=((1, 'Vinyl'), (2, 'Compact Disc')),
        initial=1,
    )
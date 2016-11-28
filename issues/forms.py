from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import IssueComment, Issue

from django.contrib.gis import forms


class CommentForm(forms.ModelForm):

    toggle_status = forms.BooleanField(required=False, label=_('toggle'))

    class Meta:
        model = IssueComment
        fields = [
            'comment',
        ]
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3})
        }


class IssueForm(forms.ModelForm):

    class Meta:
        model = Issue
        fields = [
            'point',
            'title',
            'issue_types',
            'description',
        ]
        widgets = {
            'point': forms.TextInput,
            'issue_types': forms.CheckboxSelectMultiple
        }
        help_texts = {
            'title': _('A short and descriptive title for the issue'),
            'description': _('Details of the issue'),
            'issue_types': _('Please select one or more categories for your issue')
        }

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from model_utils import Choices

from model_utils.models import TimeStampedModel


class Issue(TimeStampedModel):

    ISSUE_TYPES = Choices(
        (0, 'medical', _('medical')),
        (1, 'food', _('food and drinks')),
        (2, 'goods', _('other goods')),
        (3, 'general', _('general'))
    )

    PRIORITY_CHOICES = Choices(
        (0, 'low', _('low')),
        (1, 'normal', _('normal')),
        (2, 'high', _('high')),
        (3, 'alarm', _('alarm'))
    )

    VISIBILITY_CHOICES = Choices(
        (0, 'private', _('private')),
        (1, 'members', _('all organisation members')),
        (2, 'users', _('all registered users')),
        (3, 'public', _('public')),
    )

    title = models.CharField(max_length=300,
                             verbose_name=_('issue title'))

    description = models.TextField(blank=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    location = models.ForeignKey('organisations.Location', null=True, verbose_name='location')

    organisation = models.ForeignKey('organisations.Organisation', null=True, verbose_name=_('organisation'))

    priority = models.SmallIntegerField(choices=PRIORITY_CHOICES, default=1)
    visibility = models.SmallIntegerField(choices=VISIBILITY_CHOICES, default=3)

    @property
    def gis_location(self):
        return self.location.location if self.location else None

    class Meta:
        verbose_name = _('issue')
        verbose_name_plural = _('issues')

    def __str__(self):
        return self.title


class IssueComment(TimeStampedModel):

    issue = models.ForeignKey(Issue, related_name='comments')
    comment = models.TextField(blank=True, verbose_name=_('comment'))

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
        ordering = ['-created']

    def __str__(self):
        return 'Comment by user %s on issue #%d' % (self.created_by.username, self.issue_id)

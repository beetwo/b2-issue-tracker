from django.db import models
from django.contrib.sites.models import Site
from django.contrib.gis.db import models as geomodels
from django.utils.translation import ugettext_lazy as _


class SiteConfig(models.Model):

    site = models.OneToOneField(Site)
    issue_point = geomodels.PointField()

    area = geomodels.PolygonField()
    enforce_issue_location_in_area = models.BooleanField(
        default=False,
        help_text=_('Enforce issues to be in this sites area')
    )


    def get_extents(self):
        return self.area.extent

    def __str__(self):
        return 'Config for %s' % self.site.domain

    class Meta:
        verbose_name = _('Site Config')



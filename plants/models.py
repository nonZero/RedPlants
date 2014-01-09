from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext_lazy as _


class Family(models.Model):
    name = models.CharField(_("name"), max_length=200, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _("family")
        verbose_name_plural = _("families")

    class Meta:
        verbose_name = _('family')
        verbose_name_plural = _('families')


class IUCNLevel(object):
    EX = 6
    EW = 5
    CR = 4
    EN = 3
    VU = 2
    NT = 1
    LC = 0

    choices = (
               (LC, 'Least concern'),
               (EX, 'Extinct'),
               (EW, 'Extinct in the wild'),
               (CR, 'Critically endangered'),
               (EN, 'Endangered'),
               (VU, 'Vulnerable'),
               (NT, 'Near threatened'),
              )


class Specie(models.Model):
    family = models.ForeignKey(Family)
    name = models.CharField(_("name"), max_length=200, unique=True, db_index=True)
    common_name = models.CharField(_("common name"), max_length=200, db_index=True)
    iucn_level = models.IntegerField(_("IUCN level"),choices=IUCNLevel.choices, null=True,
                                     blank=True, db_index=True)
    details = models.TextField(_("details"), null=True, blank=True)

    def __unicode__(self):
        return self.name

    def iucn_label(self):

        if self.iucn_level is None:
            return "muted"

        if self.iucn_level > IUCNLevel.CR:
            return "danger"

        return "info"

    def get_absolute_url(self):
        return reverse("specie", args=(self.id,))

    class Meta:
        verbose_name = _('specie')
        verbose_name_plural = _('species')


class UserSpecie(models.Model):
    specie = models.ForeignKey(Specie, related_name='users')
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
                           ('specie', 'user'),
                           )

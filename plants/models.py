from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __unicode__(self):
        return self.name


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
    name = models.CharField(max_length=200, unique=True, db_index=True)
    common_name = models.CharField(max_length=200, db_index=True)
    iucn_level = models.IntegerField(choices=IUCNLevel.choices, null=True,
                                     blank=True, db_index=True)
    details = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

# encoding: utf-8
from django.db import transaction
from django.db.utils import IntegrityError
from django.test import TestCase
from plants.models import Family, Specie, IUCNLevel


class PlantsTest(TestCase):

    def test_create_species(self):
        f = Family()
        f.name = "Rosaceae"
        f.save()

        self.assertEquals(0, Specie.objects.count())

        s = Specie()
        s.family = f
        s.name = "Rosa phantasia"
        s.common_name = u"ורד דמיונית"
        s.iucn_level = IUCNLevel.EX
        s.details = u"בחיים לא ראו אותה"
        s.save()

        self.assertEquals(1, Specie.objects.count())

#         s2 = Specie()
#         s2.family = f
#         s2.name = "Rosa phantasia"
#         s2.common_name = u"ורד דמיונית"
#         s2.iucn_level = IUCNLevel.EX
#         s2.details = u"בחיים לא ראו אותה"
# 
#         self.assertRaises(IntegrityError, s2.save)
# 
#         transaction.abort()

        s2 = Specie()
        s2.family = f
        s2.name = "Rosa cooa"
        s2.common_name = u"ורד מגניבה"
        s2.details = u"ראו פעם אחת בגולן"
        s2.save()

        self.assertEquals(2, Specie.objects.count())

from django.test import TestCase

from .models import Company

class CompanyTests(TestCase):
    def test_create_company(self):
        comp = Company(name='Selenite', website='www.selenite.co')
        comp.save()
        compdb = Company.objects.filter(name='Selenite')[0] 
        self.assertEqual('Selenite', compdb.name, msg="The company name should have matched")




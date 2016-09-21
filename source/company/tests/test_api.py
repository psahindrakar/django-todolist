from django.test import TestCase

from .test_base import BaseAPITestCase

class CompanyTests(TestCase, BaseAPITestCase):
    USERNAME = 'psahindrakar'
    PASS = 'Bitroots7'
    EMAIL = 'pratik@selenite.co'
    NEW_PASS = 'Bitroots5'


    def setUp(self):
        self.init()

    
    def test_login_failed_username_validation(self):
        url = '/auth/login/'
        payload = {
            "username": self.USERNAME,
            "password": self.PASS
        }
        response = self.post(url, data=payload)
        self.assertEqual(400, response.status_code, msg="Status should have been 400 as username not provided")


    def test_create_company_api(self):
        url = '/companies/'
        payload = {
            'name' : 'Bitroots',
            'website' : 'www.bitroots.co.in'
        }
        response = self.post(url, data=payload)
        self.assertEqual(201, response.status_code, msg="Status should have been 201 CREATED")


    def test_get_company_list(self):
        url = '/companies/'
        response = self.get(url)
        self.assertEqual(200, response.status_code, msg="Status should have been 200 OK")        
        self.assertEqual(10, response.data["page_size"], msg="Page size should be 10")
        
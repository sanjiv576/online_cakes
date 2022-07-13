from django.test import TestCase
from customer.views import createForm
from django.urls import reverse, resolve
# Create your tests here.

def TestUrls(SimpleTestCase):
    def test_create_urls(self):
        url = reverse(createForm)
        self.assertEquals(resolve(url).func,createForm)
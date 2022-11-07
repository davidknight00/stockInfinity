from django.test import SimpleTestCase
from django.urls import reverse, resolve
from stockInf.views import index, account, search

# tests that urls return the valid function to render the correct page
class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_search_url(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)

    def test_account_url(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func, account)

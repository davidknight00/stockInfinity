from django.test import TestCase, Client
from django.urls import reverse
import json

class TestViews(TestCase):
    def test_index_GET(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_account_GET(self):
        client = Client()
        response = client.get(reverse('account'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account.html')

    def test_search_GET(self):
        client = Client()
        response = client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_search_POST_success(self):
        client = Client()
        response = client.post(reverse('search'), {'ticker': 'TSLA'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_seasrch_POST_failure(self):
        client = Client()
        response = client.post(reverse('search'), {'ticker': 'OMG'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, '404.html')

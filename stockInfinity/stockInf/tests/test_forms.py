from django.test import SimpleTestCase
from stockInf.forms import TickerForm

class TestForms(SimpleTestCase):
    def test_ticker_form_valid_data(self):
        form = TickerForm(data={'ticker': 'TSLA'})
        self.assertTrue(form.is_valid())

    def test_ticker_form_invalid_data(self):
        form = TickerForm(data={'ticker': 'OMGOMG'})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_ticker_form_no_data(self):
        form = TickerForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

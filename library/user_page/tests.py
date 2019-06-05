from django.test import TestCase
from .forms import BookForm


class MyTests(TestCase):
    def test_forms(self):
        form_data = {'title': 'Harry Potter', 'author': 'J. Rowling'}
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

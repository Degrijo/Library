from django.test import TestCase
from .forms import UserForm


class MyTests(TestCase):
    def test_forms(self):
        form_data = {'username': 'someone username', 'password': 'qwerty', 'first_name': 'timofei',
                     'last_name': 'ilich', 'email': 'ilick1999@gmail.com'}
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())

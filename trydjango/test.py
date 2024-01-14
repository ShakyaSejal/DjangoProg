import os 
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password

class TestSettings(TestCase):
    def test_secret_key(self):

        SECRET_KEY = os.environ.get("SECRET_KEY")
        try:
            is_strong = validate_password("SECRET_KEY")
        except Exception as e:
            msg = f"SECRET_KEY is not strong enough{e.messages}"
            self.fail(msg)
        self.assertNotEqual(settings.SECRET_KEY,"abc")
from django.test import TestCase

import sys
sys.path.append('../lists/')
from .views import home_page

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/') # 1
        self.assertTemplateUsed(response, 'home.html') # 3

from django.core.urlresolvers import reverse
from django.test import TestCase, client

class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = client.Client()

    def testHomePageLoads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def testBlogHomeTemplateUsed(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/home.html')

    def testBlogListInContext(self):
        response = self.client.get('/')
        self.assertTrue('blogpost_list' in response.context[0])

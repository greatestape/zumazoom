from django.core.urlresolvers import reverse
from django.test import TestCase, client

class HomePageTestCase(TestCase):
    fixtures = ['test.json']

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

    def testBlogPostInResponse(self):
        response = self.client.get('/')
        self.assertTrue(len(response.context[0]['blogpost_list']) > 0)
        blog_post = response.context[0]['blogpost_list'][0]
        self.assertContains(response, blog_post.title)

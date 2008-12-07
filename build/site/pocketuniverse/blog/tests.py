from django.core.urlresolvers import reverse
from django.test import TestCase, client

from blog.models import BlogPost, Category

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

    def testMonthArchiveLinkInResponse(self):
        response = self.client.get('/')
        blog_post = response.context[0]['blogpost_list'][0]
        month_archive_url = reverse('blog_archive_month', None, (),
                                    {'year': blog_post.pub_date.year,
                                     'month': blog_post.pub_date.strftime('%B').lower(),
                                     })
        self.assertContains(response, 'href="%s"' % month_archive_url)


class PostDetailTestCase(TestCase):
    fixtures = ['categories_test.json']

    def setUp(self):
        self.client = client.Client()
        self.post = BlogPost.objects.get(pk=1)

    def testDetailPageLoads(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_detail.html')

    def testPostTitleInResponse(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, self.post.title)

    def testPostHasCategoryClass(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, 'class="blog-post %s-category"' % self.post.category.slug)


class CategoryDetailTestCase(TestCase):
    fixtures = ['categories_test.json']

    def setUp(self):
        self.client = client.Client()
        self.category = Category.objects.all()[0]

    def testCategoryDetailPageLoads(self):
        response = self.client.get(reverse('blog_category_detail', None,
                                           (), {'category_slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category_detail.html')

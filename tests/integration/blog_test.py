from unittest import TestCase
from blog import Blog
from post import Post

class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog('Test', 'Test Author')


        b.create_post('Test','Test Content')

        self.assertEqual('Test', b.posts[0].title)
        self.assertEqual(1, len(b.posts))

    def test_json(self):
        b = Blog('Test', 'Test Author')
        p = Post('Test','Test Content')
        b.create_post('Test','Test Content')

        expected = {'title': 'Test', 'author': 'Test Author', 'posts': [{'title': 'Test', 'content': 'Test Content'}]}

        self.assertDictEqual(expected, b.json())

from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test Blog', 'Test Author')

        self.assertEqual('Test Blog', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Test Author')
        expected = 'Test by Test Author (0 posts)'

        self.assertEqual(expected, b.__repr__())

from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual("Test Content", p.content)

    def test_repr(self):
        p = Post('Test', 'Test Content')
        expected = '<Post: Test>'

        self.assertEqual(expected, p.__repr__())

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, p.json())

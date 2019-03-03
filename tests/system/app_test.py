from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test Blog', 'Test Author')
        app.blogs = {'Test Blog': blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')

                app.menu()
                mocked_ask_create_blog.assert_called()

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')

                app.menu()
                mocked_print_blogs.assert_called()

    def test_menu_calls_ask_read_blog(self):
        blog = app.blogs['Test Blog']
        blog.create_post('Test Post 1', 'Test Content 1')
        with patch('app.print_posts') as mocked_print_posts:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('r', 'Test Blog', 'Test Post 1', 'q')
                app.menu()

                mocked_print_posts.assert_called_with(blog)

    def test_menu_calls_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'Test Blog', 'Test Post', 'Test Content', 'q')

            app.menu()

            self.assertEqual(app.blogs['Test Blog'].posts[0].title, 'Test Post')
            self.assertEqual(app.blogs['Test Blog'].posts[0].content, 'Test Content')

    def test_menu_input(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called()

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        blog = app.blogs['Test Blog']
        with patch('builtins.input', return_value='Test Blog'):
            blog.posts.append({'title': 'Test Post 1', 'content': 'Test Content 1'})
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = app.blogs['Test Blog']
        post = {'title': 'Test Post 1', 'content': 'Test Post 2'}
        blog.posts.append({'title': 'Test Post 1', 'content': 'Test Post 2'})

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(post)

    def test_print_post(self):
        post = Post('Test Post 1', 'Test Content 1')
        expected_print = '--- Test Post 1 ---\nTest Content 1\n'

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = app.blogs['Test Blog']
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test Blog', 'Test Post 1', 'Test Content 1')

            app.ask_create_post()
            self.assertEqual(blog.posts[0].title, 'Test Post 1')
            self.assertEqual(blog.posts[0].content, 'Test Content 1')

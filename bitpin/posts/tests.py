from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from bitpin.posts.models import Post, RatePost


class PostAPITestCase(APITestCase):

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='ali', password='123')
        self.client = APIClient()

    def test_create_post(self):
        """Test creating a new post"""
        data = {
            'title': 'New Post',
            'body': 'hello.'
        }
        response = self.client.post('/api/create-post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')

    def test_list_posts(self):
        """Test listing all posts"""
        Post.objects.create(user=self.user, title='Test Post 1', body='This is test post 1.')
        Post.objects.create(user=self.user, title='Test Post 2', body='This is test post 2.')
        response = self.client.get('/api/list-posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Post 1')
        self.assertEqual(response.data[1]['title'], 'Test Post 2')

    def test_rate_post(self):
        """Test rating a post"""
        self.client.login(username='testuser', password='testpassword')
        post = Post.objects.create(user=self.user, title='Test Post', body='This is a test post.')
        data = {
            'post': post.id,
            'rate': 5
        }
        response = self.client.post('/api/rate-post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RatePost.objects.count(), 1)
        self.assertEqual(RatePost.objects.get().rate, 5)
        self.client.logout()

    def test_create_post_unauthenticated(self):
        """Test creating a post without authentication"""
        data = {
            'title': 'Test Post',
            'body': 'This is a test post.'
        }
        response = self.client.post('/api/create-post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_rate_post_unauthenticated(self):
        """Test rating a post without authentication"""
        post = Post.objects.create(user=self.user, title='Test Post', body='This is a test post.')
        data = {
            'post': post.id,
            'rate': 4
        }
        response = self.client.post('/api/rate-post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_rate_nonexistent_post(self):
        """Test rating a non-existent post"""
        self.client.login(username='testuser', password='testpassword')
        data = {
            'post': 999,
            'rate': 3
        }
        response = self.client.post('/api/rate-post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.client.logout()

    def test_invalid_rate_value(self):
        """Test rating a post with an invalid rate value"""
        self.client.login(username='testuser', password='testpassword')
        post = Post.objects.create(user=self.user, title='Test Post', body='This is a test post.')
        data = {
            'post': post.id,
            'rate': 10  # Invalid rate value
        }
        response = self.client.post('/api/rate-post/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.client.logout()

from django.urls import reverse
from django.test import SimpleTestCase, TestCase
from django.contrib.auth import get_user_model

from .models import Task

class HomePageTest(SimpleTestCase):
    def test_home_page_template(self):
        request = self.client.get('/')

        self.assertTemplateUsed(request, 'home.html')


    def test_home_page_status_code(self):
        request = self.client.get(reverse('home'))

        self.assertEqual(request.status_code, 200)

    
    def test_home_page_url_name(self):
        request = self.client.get(reverse('home'))

        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'home.html')


class TestTaskCreation(TestCase):
    def setUp(self):
        self.testuser = get_user_model().objects.create(
            username='testuser',
            email='test@mail',
            password='secret',
            age=20,
            )

        self.new_task = Task.objects.create(
            title='test task',
            owner=self.testuser
            )
        

    def test_task_creation_user_not_logged(self):
        request = self.client.get('/new/')

        self.assertEqual(request.status_code, 302)


    def test_task_creation_status_code(self):
        self.client.force_login(self.testuser)
        request = self.client.get(reverse('task_new'))

        self.assertEqual(request.status_code, 200)


    def test_task_creation_template(self):
        self.client.force_login(self.testuser)
        
        request = self.client.get(reverse('task_new'))

        self.assertTemplateUsed(request, 'task_new.html')

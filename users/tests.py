from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class SignUpPageTest(TestCase):
    
    def setUp(self):
        self.test_user = get_user_model().objects.create(
            username='testuser',
            email='test@mail',
            password='secret',
            age=20,
            )


    def test_signup_url_by_name(self):
        request = self.client.get(reverse('signup'))

        self.assertEqual(request.status_code, 200)


    def test_signup_status_code(self):
        request = self.client.get(reverse('signup'))

        self.assertEqual(request.status_code, 200)


    def test_signup_template(self):
        request = self.client.get(reverse('signup'))

        self.assertTemplateUsed(request, 'signup.html')


    def test_signup_form(self):
        testuser = get_user_model().objects.create_user('testuser1', 'test@mail.com')

        self.assertEqual(get_user_model().objects.all().count(), 2)
        self.assertEqual(get_user_model().objects.all()[1].username, 'testuser1')
        self.assertEqual(get_user_model().objects.all()[1].email, 'test@mail.com')
    
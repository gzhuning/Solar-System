from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class AuthenticationFlowTests(TestCase):
    def test_signup_creates_and_signs_in_student(self):
        response = self.client.post(
            reverse('solar_system:signup'),
            {
                'username': 'newstudent',
                'password1': 'StudyHub-Student-482!',
                'password2': 'StudyHub-Student-482!',
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome, <strong>newstudent</strong>.')
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_and_logout(self):
        user = get_user_model().objects.create_user(
            username='returningstudent',
            password='StudyHub-Student-482!',
        )

        login_response = self.client.post(
            reverse('solar_system:login'),
            {'username': user.username, 'password': 'StudyHub-Student-482!'},
            follow=True,
        )
        self.assertEqual(login_response.status_code, 200)
        self.assertContains(login_response, 'Welcome, <strong>returningstudent</strong>.')

        logout_response = self.client.post(reverse('solar_system:logout'), follow=True)
        self.assertEqual(logout_response.status_code, 200)
        self.assertContains(logout_response, 'Sign up')
        self.assertNotContains(logout_response, 'Welcome, <strong>returningstudent</strong>.')

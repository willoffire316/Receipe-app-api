from django.test import TestCase
from django.contrib.auth import get_user_model 


class ModelTest(TestCase):
    """Unit test for custom usr model"""

    def test_create_user_with_email(self):
        email = "test_sample_123a@gmail.com"
        password = "test_sample_123"

        # creating the user 

        user = get_user_model().objects.create_user(
            email = email, 
            password = password
        )

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_normalize(self):
        """test the email for the new email normalized"""
        email = "testuser@LONDON.com"
        user = get_user_model().objects.create_user(email, "sample")
        self.assertEquals(user.email, email.lower())



    def test_new_user_invalidemail(self):
        """test creating user with no email , raise error """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')


    def test_create_newsuper_user(self):
        """Create super user""" 
        user = get_user_model().objects.create_superuser(
            email = "master@gmail.com", 
            password ="master"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
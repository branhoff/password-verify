from password_verify import app
import unittest

class FlaskTestCase(unittest.TestCase):
    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the password-tester page loads correctly
    def test_load(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertTrue(b'Password Tester' in response.data)

    # Ensure that the password-tester behaves correctly given correct credentials
    def test_norm_pass_correct(self):
        tester = app.test_client(self)
        response = tester.post('/register', data=dict(password='password123'))
        self.assertFalse(b'INVALID' in response.data)

        # capital letters with numbers
        response = tester.post('/register', data=dict(password='PassWord123'))
        self.assertFalse(b'INVALID' in response.data)

        # capital letters with numbers
        response = tester.post('/register', data=dict(password='Pass863Word'))
        self.assertFalse(b'INVALID' in response.data)

        # capital letters with numbers
        response = tester.post('/register', data=dict(password='P123456789'))
        self.assertFalse(b'INVALID' in response.data)

        # numbers in front, lowercase letter at end
        response = tester.post('/register', data=dict(password='123456789p'))
        self.assertFalse(b'INVALID' in response.data)

        # letters in middle
        response = tester.post('/register', data=dict(password='123abc89'))
        self.assertFalse(b'INVALID' in response.data)

        response = tester.post('/register', data=dict(password='password123'))
        self.assertFalse(b'INVALID' in response.data)

    # Ensure that the password-tester behaves correctly given incorrect credentials
    def test_norm_pass_incorrect(self):
        tester = app.test_client(self)
        # too short lower case, no numbers
        response = tester.post('/register', data=dict(password='test'))
        self.assertTrue(b'Field must be at least 8 characters long' in response.data)

        response = tester.post('/register', data=dict(password='test'))
        self.assertTrue(b'Field must contain at least one digit' in response.data)

        # too short lower case w/ numbers
        response = tester.post('/register', data=dict(password='test123'))
        self.assertTrue(b'Field must be at least 8 characters long' in response.data)

        # too short lower case w/ numbers
        response = tester.post('/register', data=dict(password='test123'))
        self.assertTrue(b'Field must be at least 8 characters long' in response.data)

        # correct length all lower case, no numbers
        response = tester.post('/register', data=dict(password='testtest'))
        self.assertTrue(b'Field must contain at least one digit' in response.data)

        # correct length all numbers
        response = tester.post('/register', data=dict(password='123456789'))
        self.assertTrue(b'Field must contain at least one letter' in response.data)

    def test_admin_pass_correct(self):
        tester = app.test_client(self)
        response = tester.post('/register', data=dict(password='password123@!@%'))
        self.assertFalse(b'Field must be at least 13 characters long' in response.data)
        self.assertFalse(b'Field must contain at least one special character' in response.data)
        self.assertFalse(b'Field must contain at least one digit' in response.data)
        self.assertFalse(b'Field must contain at least one letter' in response.data)

        response = tester.post('/register', data=dict(password='!@#$%^&*1a'))
        self.assertFalse(b'Field must be at least 13 characters long' in response.data)
        self.assertFalse(b'Field must contain at least one special character' in response.data)
        self.assertFalse(b'Field must contain at least one digit' in response.data)
        self.assertFalse(b'Field must contain at least one letter' in response.data)

    # Ensure that the password-tester behaves correctly given incorrect credentials
    def test_admin_pass_incorrect(self):
        tester = app.test_client(self)
        # too short lower case, no numbers
        response = tester.post('/admin', data=dict(password='test'))
        self.assertTrue(b'Field must be at least 13 characters long' in response.data)
        self.assertTrue(b'Field must contain at least one special character' in response.data)
        self.assertTrue(b'Field must contain at least one digit' in response.data)

        # too short lower case w/ numbers
        response = tester.post('/admin', data=dict(password='test123'))
        self.assertTrue(b'Field must be at least 13 characters long' in response.data)

        # too short lower case w/ numbers
        response = tester.post('/admin', data=dict(password='test123'))
        self.assertTrue(b'Field must be at least 13 characters long' in response.data)

        # correct length all lower case, no numbers
        response = tester.post('/admin', data=dict(password='testtest'))
        self.assertTrue(b'Field must contain at least one digit' in response.data)

        # correct length all numbers
        response = tester.post('/admin', data=dict(password='123456789'))
        self.assertTrue(b'Field must contain at least one letter' in response.data)
        self.assertTrue(b'Field must contain at least one special character' in response.data)
        self.assertTrue(b'Field must be at least 13 characters long' in response.data)

        response = tester.post('/admin', data=dict(password='<>'))
        self.assertTrue(b'Field must contain at least one letter' in response.data)
        self.assertTrue(b'Field must contain at least one special character' in response.data)
        self.assertTrue(b'Field must be at least 13 characters long' in response.data)
        self.assertTrue(b'Field must contain at least one digit' in response.data)

if __name__ == '__main__':
    unittest.main()
# /services/users/project/tests/test_users.py

import json
import unittest
from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
    def test_add_user(self):
        '''Check if user is added correctly'''
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps({
                    'username': 'rizvan',
                    'email': 'rizvan@mail.lt'
                }),
                content_type='application/json',
            )
            self.assertEqual(response.status_code, 201)

    def test_get_user_list(self):
        '''Check if correct user list is returned'''


if __name__ == '__main__':
    unittest.main()

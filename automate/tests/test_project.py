# automate/server/tests/test_main.py


import unittest

from base import BaseTestCase
from automate.server.models import Project
from automate.server import app, db
import random, string

class TestMainBlueprint(BaseTestCase):

   #def test_index(self):
   #    # Ensure Flask is setup.
   #    response = self.client.get('/', follow_redirects=True)
   #    self.assertEqual(response.status_code, 200)
   #    self.assertIn(b'Welcome!', response.data)
   #    self.assertIn(b'Register/Login', response.data)

    #def test_about(self):
    #    # Ensure about route behaves correctly.
    #    response = self.client.get('/about', follow_redirects=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertIn(b'About', response.data)

    #def test_404(self):
    #    # Ensure 404 error is handled.
    #    response = self.client.get('/404')
    #    self.assert404(response)
    #    self.assertTemplateUsed('errors/404.html')

    def test_get_project_by_id(self):
        id = 1
        response = self.client.get('/project/'+id, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_insert_project(self):
        id = 1
        response = self.client.get('/project/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #ef test_update_project_by_id(self):
    #   id = 1
    #   response = self.client.get('/project/'+id, follow_redirects=True)
    #   self.assertEqual(response.status_code, 200)

    #ef test_delete_project_by_id(self):
    #   id = 1
    #   response = self.client.get('/project/'+id, follow_redirects=True)
    #   self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()

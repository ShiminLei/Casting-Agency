import os
import unittest
import json
import random
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Artist, Song, songs


TEST_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
CASTING_ASSISTANT = os.getenv('CASTING_ASSISTANT')
CASTING_MANAGER = os.getenv('CASTING_MANAGER')


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.casting_assistant = CASTING_ASSISTANT
        self.casting_manager = CASTING_MANAGER
        setup_db(self.app, TEST_DATABASE_URI)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

    '''
    RBAC TEST
    '''

    def test_post_artists_by_manager_with_auth_200(self):
        response = self.client().post('/artists',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.executive_producer)
                                      },
                                      json={
                                          "name": "Edward",
                                          "gender": "male",
                                          "age": 25,
                                      })
        data = json.loads(response.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status_message'], 'OK')


    def test_post_songs_by_manager_with_auth_200(self):
        response = self.client().post('/songs',
                                      headers={
                                          "Authorization": "Bearer {}"
                                          .format(self.executive_producer)
                                      },
                                      json={
                                          "title": "Love Song",
                                          "genre": "Blue",
                                          "release_date": "2015-01-01"
                                      })

        data = json.loads(response.data)

        self.assertEqual(data['success'], True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status_message'], 'OK')


if __name__ == '__main__':
    unittest.main()

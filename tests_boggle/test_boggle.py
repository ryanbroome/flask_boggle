from unittest import TestCase
from app import app, score
from flask import session
from boggle import Boggle

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class BoggleTests(TestCase):
    def test_home(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertIn('<a href="/">Home</a>', html)
            self.assertEqual(resp.status_code, 200)
            
    def test_boggle_load(self):
        with app.test_client() as client:
            resp = client.get('/boggle')
            html = resp.get_data(as_text=True)

            self.assertIn('<h1>Boggle Board</h1>', html)

    def test_boggle_board(self):
        with app.test_client() as client:
            resp = client.get('/boggle')
            html = resp.get_data(as_text=True)

            self.assertEqual(type(Boggle.make_board(self)) == list, True)
            self.assertIn("<table>", html)

    def test_boggle_score(self):
        with app.test_client() as client:
            resp = client.get('/reset')
            html = resp.get_data(as_text=True)

            self.assertIn("<h3>Score: 0</h3>", html)
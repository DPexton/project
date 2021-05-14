import unittest
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase

from application import app, db
from application.models import Teams, Players

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI=getenv("DATABASE_URI")
            SECRET_KEY="SECRET_KEY
            DEBUG=True"
        )
        
        return app
    def setup(self):
        db.create_all()
        db.session.add()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code,200)

    def test_createteam_get(self):
        response = self.client.get(url_for('create_team', id=1))
        self.assertEqual(response.status_code,200)

    def test_createplayer_get(self):
        response = self.client.get(url_for('create_player', id=1))
        self.assertEqual(response.status_code,200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update_team', id=1))
        self.assertEqual(response.status_code,200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1))
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_teams(self):
        response = self.client.get(url_for('home'))
        self.assertIn(b"",response.data)

class TestCreate(TestBase):
    def test_create_team(self):
        response = self.client.post(url_for(
            "create_team"),
            data=dict(team="celtic"),
            follow_redirects=True
        )
        self.assertIn(b"celtic", response.data)

    def test_create_player(self):
        response = self.client.post(url_for(
            "create_player"),
            data=dict(team="celtic"),
            follow_redirects=True
        )
        self.assertIn(b"celtic", response.data)

class TestUpdate(TestBase):
    def test_update_team(self):
        response = self.client.post(
            url_for("update_team"),
            data=dict(description= ""),
            follow_redirects=True
        )
        self.assertIn(b"", response.data)


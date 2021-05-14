import unittest
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase
from os import getenv

from application import app, db
from application.models import Teams, Players

class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            [SQLALCHEMY_DATABASE_URI]=getenv("DATABASE_URI")
            [SECRET_KEY]=getenv("SECRET_KEY")
            DEBUG=True"
        )
        return app
   
    def setup(self):
        db.create_all()
        test_team = Teams(team_name = "Celtic FC",
            test_city = "Glasgow"
            )
        test_player = Players(player_name = "Kristofer Ajer", 
            skill = "73", 
            position = "LB"
            )
        db.session.add(test_team)
        db.session.commit(test_player)

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
        self.assertIn(b"Celtic Fc",response.data)
        self.assertIn(b"Glasgow",response.data)

class TestCreate(TestBase):
    def test_create_team(self):
        response = self.client.post(url_for(
            "create_team"),
            data=dict(form_team_name="Arsenal FC",
            form_city = "London")
            follow_redirects=True
            )
        self.assertIn(b"Arsenal FC", response.data)
        self.assertIn(b"London", response.data)

    def test_create_player(self):
        response = self.client.post(url_for(
            "create_player", id=1),
            data=dict(form_player_name ="Kieran Tierney",
            form_playerskill = "81",
            form_position = "LW")
            follow_redirects=True
            )
        self.assertIn(b"Kieran Tierney", response.data)
        self.assertIn(b"81", response.data)
        self.assertIn(b"LW", response.data)

class TestUpdate(TestBase):
    def test_update_team(self):
        response = self.client.post(url_for(
            "update_team" id=1),
            data=dict(form_team_name="Manchester Utd",
            form_city = "Manchester")
            follow_redirects=True
            )
        self.assertIn(b"Manchester Utd", response.data)
        self.assertIn(b"Manchester", response.data)

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Celtic FC", response.data)
        self.assertNotIn(b"Glasgow")


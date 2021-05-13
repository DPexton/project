from application import db
from datetime import datetime

class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), nullable=False)
    overall_skill = db.Column(db.Integer, nullable=False)
    date_formed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    players = db.relationship('Players', backref='team')

class Players(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    position = db.Column(db.String(10), nullable=False)
    skill = db.Column(db.Integer, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)

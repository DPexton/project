from application import db
from datetime import datetime

class Teams(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(30), Nullable=False)
    overall_skill = db.Column(db.Integer, Nullable=False)
    date_formed = db(Column.Datetime, Nullable=False, default=datetime.utcnow)
    players = db.relationship('Team', backref='player')

class Players(db.Model):
    player_id = db.Column(db.Integer, Primary_key=True)
    player_name = db.column(db.String(50), Nullable=False)
    position = db.Column(db.String(10), Nullable=False)
    skill = db.Column(db.Integer, Nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False

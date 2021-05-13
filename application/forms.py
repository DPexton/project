from flask_wtf import FlaskForm 
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class TeamForm(FlaskForm):
    form_team_name = StringField("Please enter the name of your Team", validators=[DataRequired()])
    form_city = StringField("Please enter the City your team is from", validators=[DataRequired()]) 
    submit = SubmitField('new_team')

class PlayerForm(FlaskForm):
    form_player_name = StringField("Please Enter the full name of your player", validators=[DataRequired()])
    form_playerskill = IntegerField("Please Enter the skill level of your player between 1 and 100", validators=[NumberRange(min=1, max=100, message="enter a number between 1 & 100")] )
    form_position = SelectField("Please select your players position", choices=[
        ("GK", "Goalkeeper"),
        ("RB", "Right Back"),
        ("LB", "Left Back"),
        ("CB", "Center Back"),
        ("RW", "Right Wing"),
        ("LW", "Left Wing"),
        ("CM", "Central Midfield"),
        ("CAM", "Centre Attack Midfield"),
        ("ST", "Striker")
        ])
    submit = SubmitField('create player')

class UpdateTeam(FlaskForm):
    form_team_name = StringField("Please enter the new name of your Team", validators=[DataRequired()])
    form_city = StringField("Please enter the City your team is from", validators=[DataRequired()]) 
    submit = SubmitField('create team')

class UpdatePlayer(FlaskForm):
    form_player_name = StringField("Please Enter the full name of your player", validators=[DataRequired()])
    form_playerskill = IntegerField("Please Enter the skill level of your player between 1 and 100", validators=[NumberRange(min=1, max=100, message="enter a number between 1 & 100")] )
    form_position = SelectField("Please select your players position", choices=[
        ("GK", "Goalkeeper"),
        ("RB", "Right Back"),
        ("LB", "Left Back"),
        ("CB", "Center Back"),
        ("RW", "Right Wing"),
        ("LW", "Left Wing"),
        ("CM", "Central Midfield"),
        ("CAM", "Centre Attack Midfield"),
        ("ST", "Striker")
        ])
    submit = SubmitField('create player')
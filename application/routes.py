from application import app, db
from application.models import Teams, Players
from application.forms import TeamForm, PlayerForm
from flask import render_template

@app.route("/")
@app.route("/home")
def home():
    all_teams = Teams.query.all()
    all_players = Players.query.all()
    return render_template("home.html", title="Home", all_teams=all_teams)

@app.route("/create_team", methods=['GET', 'POST'])
def create_team():
    form=TeamForm()
    if form.validate_on_submit():
        new_team = Teams(
            team_name = form.form_teamname.data, 
            city = form.form_city.data
            )
        db.session.add(new_team)  
        db.session.commit() 
        return f"{new_team.team_name} successfully created!"
    return render_template("create_team.html", title = "Create a Team", form=form) 

@app.route("/create_player/<int:id>", methods=['GET', 'POST'])
def create_player(id): 
    form=PlayerForm
    if form.validate_on_submit():
        new_player = Players(
            player_name = form.form_playername.data, 
            skill = form.form_playerskill.data,
            position = form.form_position.data,
            team_id = id
            )
        db.session.add(new_player)  
        db.session.commit() 
        return f"{new_player.player_name} successfully added!"
    

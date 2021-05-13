from os import removedirs
from application import app, db
from application.models import Teams, Players
from application.forms import TeamForm, PlayerForm
from flask import render_template, request, redirect, url_for

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    all_teams = Teams.query.all()
    all_players = Players.query.all()
    return render_template("home.html", title="Home", all_teams=all_teams)

@app.route("/create_team", methods=['GET', 'POST'])
def create_team():
    form=TeamForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_team = Teams(
            team_name = form.form_team_name.data, 
            city = form.form_city.data
            )
            db.session.add(new_team)  
            db.session.commit() 
            return redirect(url_for("home"))
    return render_template("create_team.html", title = "Create a Team", form=form) 

@app.route("/create_player/<int:id>", methods=['GET', 'POST'])
def create_player(id): 
    form=PlayerForm
    team = Teams.query.filter_by(id=id).first()
    if request.method == "POST":
        if form.validate_on_submit():
            new_player = Players(
            player_name = form.form_playername.data, 
            skill = form.form_playerskill.data,
            position = form.form_position.data,
            team_id = id
            )
            db.session.add(new_player)  
            db.session.commit() 
            return redirect(url_for("home"))
    return render_template("create_player.html", title = "Create a player", form=form) 

app.route("/deleteteam/<int:id>")
def delete(id):
    player = Teams.query.filter_by(id=id).first()
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for("home"))
    
    
    
@app.route("/deleteplayer/<int:id>")
def deletesequence(id):
    task = Players.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))
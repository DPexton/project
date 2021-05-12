from application import app, db
from application.models import Teams Players

@app.route("/")
@app.route("/home")
def home():
    all_teams = Teams.query.all()
    all_players = Players.query.all()
    return str(all)

@app.route("/create_team")
def create_team():
    new_team = Teams(team_name = "Team Name" , overall_skill = "Overall skill" )
    db.session.add(new_team)
    db.session.commit()
    return "A new team has been added!"

@app.route("/create_player")
def create_player():
    new_player = Players(player_name = "Player Name" , position = "Player Position" , skill = "Player Skill Level")
    db.session.add(new_player)
    db.session.commit()
    return "A new player has been added!"

@app.route("/update/<int:id>")
def update(player_id):
    player = Player.query.filter(id = player_id).first()
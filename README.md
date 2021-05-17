# README - Project 

## Contents

## Brief

## Introduction

### The Brief

The Objective of this project was:

* To create a CRUD application with utilisation of supporting tools,
methodologies and technologies that encapsulate all core modules
covered during training.

This application must include the Create, Read, Update and Delete functions to show my progress over the past month. Along with this there were several documentary requirements, such as:

* An Entity Relationship Diagram
* A Trello/Kanban board
* Risk Assessment
* CI (Continuous Integration) documentation
* A working website built using Flask and HTML

My project was also built as per the brief. Using a GitHub repository as a VCS and working through a virtual machine.

### My Objective

I chose to make a program that would allow football enthusiasts to create view a table of football teams. This would allow them to create the teams, players and update attributes of the individual teams.

CRUD Implementations:

* Create:   
  * Individual Football Teams including details of the teams home city and date of creation.
  * Players which can be assigned to a specific team. Including details of position and skill level.
* Read:
  * All Teams and Players created
* Update:
  * The name and home city of a given team.
* Delete:
  * Specific teams and the players assigned to said team.

I also looked into some other features for the application. This included the ability to update and delete specific players and also a match system using an overall skill attribute for each team to allow for teams to be compared and a winner to be selected. Due to time constraints, these are not included in the current build.
## Architecture

### Risk Assessment

My Risk assessment is shown below:

![](https://imgur.com/U8lSauw)

The highlighted row represents a risk that only crossed my path after facing my own technical issues and thus required updating the risk assessment.

Here is also a link to my [Risk Assessment](#https://qalearning-my.sharepoint.com/:i:/r/personal/dpexton_qa_com/Documents/Risk%20Assessment.png?csf=1&web=1&e=dxQejr_).

### Trello Board

I used the site Trello as a Project Tracking tool.    
I used this as it is a familiar and easy to use application which makes for clear visibility of project goals and aesthetically fits very well into a presentation.

![](https://i.imgur.com/NbUXol2.png)

As you can see on the board, each of the projects user stories were categorized. Green were high priority, yellow were non-essential however within scope, Red was stories that were likely out of scope however potentially feasable in a future build.      
   
Here is a link to the [Full Board](https://qalearning-my.sharepoint.com/:i:/r/personal/dpexton_qa_com/Documents/Project%20Tracking.png?csf=1&web=1&e=gU2AEA)

### Entity Relationship Diagram

![](https://imgur.com/4BmcEpA)

As you can see for the diagram we have two tables. Teams and Players, they are connected by a one-to-many relationship due to the fact that each of the players can only be assigned to one team.

This relationship allows users to easily view each team and the players contained within. Allowing for easy management.

The highlighted section in the diagram shows the original plan for the "Matches" table, this would be used to allow the aformentioned functionality to compare the skill levels of teams. Due to the time constraints these were not deemed feasable for the current build.   
This also applies to the highlighted "Overall skill" attribute as this was at the core of the "Matches" concept



## Testing

I used PyTest in order to run unit tests which will test each function in the apoplication to ensure that the output is correct each time. Below I have included a screenshot of the coverage report provided by Jenkins:

![](https://imgur.com/a/d9HhXup)

As you can see the application has achieved 100% coverage through unit testing

The Jenkins script for my unit tests contains several steps:

* 1 - Installing the virtual environment   
```
python3 -m venv venv   
source venv/bin/activate
```

* 2 - Installing all the required modules for the application   
```
pip3 install -r requirements.txt
```

* 3 Installing PyTest
```
pip3 install pytest pytest-cov
```

* 4 - Running the unit tests
```
python3 -m pytest --cov=application
```

## Front End

### Home Page

Below you will see the front page of my application. This is navigared to using /home or an unspecified path.    

From here we can see the currently available options which initially are simply to refresh the home page or to add a team.

This navigation bar is contained in a layout template. making it available on every page.

![](https://imgur.com/0GKzf4t)

### Create a Team
This is the screen we see when we select the "Add Team" option.   
As you can see we can enter the name of the team and the teams home City.   
When a team is created a timestamp is also saved to represent the date that the team was created.

![](https://imgur.com/6ZxnQnU)

Once the team is created we see an updated homepage which shows the options available for this team, to add a player, update or delete the team.

![](https://imgur.com/AVTqKPA
)
### Create a Player
On this screen we are able to add a player. By selecting the Create player option next to the desired team. This ensures that this new player will be assigned to the selected team.   

Here we can add player details such as Name, Position and skill level.

![](https://imgur.com/YY8zwPc)

Once submitted this player will be added to the selected team and the user will be redirected to the homepage where the player will now be displayed underneath their respective team as shown below.

![](https://imgur.com/tI2nhf9)

### Update a Team

By selecting the Update team option next to each team, we can change the team name and home city.

![](https://imgur.com/AvrJn6g)

Once the details are entered and the Update Team button is clicked, the changes are submitted and the user is redirected to the homepage.    
The final home page is displayed below.   

![](https://imgur.com/YbVeYOG) 

## Footer

### Future Improvements

* As mentioned in my Introduction, in a future build I would look to implement an "overall skill" attribute into the Teams table. This would take an average of the skill of each player and output overall skill for the team.   
* A third table called "Matches" would ideally be implemented into a future build containing a function that would take the overall skill of two selected teams and output a winner based on skill.   
This would allow for easy comparisons if the database reached a larger number of teams.

### Author
Dafydd Pexton

### Acknowledgements

Harry Volker   
Oliver Nichols
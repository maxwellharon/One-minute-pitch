# THE PITCH APP

 The Pitch app App allows a user to be registered members of the app so that they can post pitches and other users can comment on them, downvote and upvote.
#### By **Derrick** created on, May 19th 2018 

## Description
This Application is python based and runs on any browser, It allows a user to be registered members of the app so that they can post pitches and other users can comment on them, downvote and upvote and view the various pitch categories eg promotion and pickup lines. Anonymous users can only view categories but cannot comment on them.

## Behaviour of the application

### Development and Setup.
### prerequisites
+ First clone the project to your camputer. ```git clone <repo url>```
+ Ensure python3 is installed.
+ Install virtual environment by running ```pip3 install virtualenv```
+ Create a virtualenvironment by running ``` virtualenv <name of environment>``` on the terminal and once its activated by running ``` source <name of environment>/bin/activate``` then install all the packages by running ```pip3 install -r requirements.txt```
+ Then start the server by running ```python3 manage.py runserver```.
+ Copy the link and paste in any browser ```http://localhost:5000```

## Authentication

+ Once the url is entered the user is welcomed to the app and redirected to the registration and login form. 
- If the user is anonymouse, He/she can only view the categories and can't vote or comment.
- If the user on the the other hand is Authnticated but logged out, can login again to interact with the app by entering email and password details into a form.
- The user last option is to register using a unique username and a password after which the user is redirected to login to the app.
- Once the user is authenticated, can logout at will.

## Pitches.

+ The user Can add pitches and they get displayed from the most resent one.
+ The user can upvote,downvote and comment on a pitch.
+ The pitch information is displayed alongside other pitches, a pitch contains information such as pitch body, pithch author, downvotes,upvotes and total vote count.
+ The user can click the author of the pitch to view all their information such as their bio, profile picture and all their pitches.

## Categories

+ The pitches are categorized as punchline, product, intrview and promotion pitches.
+ The user can view all these categories whether authenticated or not.


### Important packages used in app development.

```
certifi==2018.4.16
chardet==3.0.4
click==6.7
dominate==2.3.1
Flask==1.0.2
Flask-Bootstrap4==4.0.2
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
idna==2.6
itsdangerous==0.24
Jinja2==2.10
MarkupSafe==1.0
requests==2.18.4
visitor==0.1.3
Werkzeug==0.14.1

```
## Technology Used
+ Python3.6

## Test Driven Development
Testing was done using python inbuild test tool called **unittest** to test database and form models.

## Bugs and Development.
+ SQL errors especially when the user deletes a post.


## Further help
To get Further help you can visit the official [python](https://www.python.org/) and [flask](http://flask.pocoo.org/ ) documentation.

## Licence
MIT (c) 2017 [muriithi derrick](https://github.com/muriithiderro)

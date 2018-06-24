rom flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_socketio import SocketIO ,send
from flask_moment import Moment


# instance of the database
db = SQLAlchemy()
bootstrap = Bootstrap()
bcrypt=Bcrypt()
photos = UploadSet('photos',IMAGES)

simple = SimpleMDE()
socketio = SocketIO()
moment = Moment()


login_manager = LoginManager()
login_manager.session_protection='strong'
login_manager.login_view = 'auth.login'

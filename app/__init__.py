from flask import Flask
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


def create_app(config_name):
	"""this function initializes the app when called from manage.py file"""

	app = Flask(__name__)
	app.config.from_object(config_options[config_name])

	# database initialization
	db.init_app(app)

	# bootstrap
	bootstrap.init_app(app)

	# bcrypt
	bcrypt.init_app(app)

	# login
	login_manager.init_app(app)

	# blueprints
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint,url_prefix='/authenticate')

	# photos configurations
	configure_uploads(app,photos)

    #simple markdown initialization
	simple.init_app(app)

	#socketio initialization
	socketio.init_app(app)

	#flask moment initialization
	moment.init_app(app)

	# import and register blueprints
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app

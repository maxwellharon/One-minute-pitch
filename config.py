import os

class Config:
	# SECRET_KEY = os.environ.get('17dc65f0ff74785949903bf317fe8ef2')
	SECRET_KEY = '17dc65f0ff74785949903bf317fe8ef2'
	# secret
	SQLALCHEMY_TRACK_MODIFICATIONS=True
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
		# "postgresql://postgres:postgres@localhost/pitch"
	UPLOADED_PHOTOS_DEST = "app/static/photos"

	# email configurations
	MAIL_SERVER = 'smtp.google.cpm'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('maxwellharon54@gmail.com')
	MAIL_PASSWORD = os.environ.get("mustangBEAST7")


	# simple mde configurations
	SIMPLEMDE_JS_IIFE = True
	SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
	DEBUG=False

class DevConfig(Config):
	DEBUG = True

class TestConfig(Config):
	SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/test_pitch"

config_options = {
	'development':DevConfig,
	'production':ProdConfig,
	'test': TestConfig,
	'default':ProdConfig
}

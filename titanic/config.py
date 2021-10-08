import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

#Postgres SQLL URL

postgressql_url = "postgresql://" + os.getenv('POSTGRES_USER') + ":" + os.getenv('POSTGRES_PASSWORD') + "@"+os.getenv('POSTGRES_HOST')+":"+os.getenv('POSTGRES_PORT')+"/" + os.getenv('POSTGRES_DB')
# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = postgressql_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SqlAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
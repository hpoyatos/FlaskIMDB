from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#Instanciar os dois objetos
db = SQLAlchemy()
migrate = Migrate()

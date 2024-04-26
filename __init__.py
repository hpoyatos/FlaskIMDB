from flask import Flask 
from .extensions import db, migrate, Moment, FlaskForm, StringField, SubmitField
#adiciona isso
from .routes.maraBp import maraBp
import pytz
from datetime import datetime

import pytz
from pytz import timezone
import tzlocal 

def datetimefilter(value, format="%I:%M %p"):
    tz = pytz.timezone('America/Sao_Paulo') # timezone you want to convert to from UTC
    utc = pytz.timezone('UTC')  
    value = utc.localize(value, is_dst=None).astimezone(pytz.utc)
    local_dt = value.astimezone(tz)
    return local_dt.strftime(format)


import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__)
    app.config['TIMEZONE'] = 'America/Sao_Paulo'
    app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'
    app.jinja_env.filters['datetimefilter'] = datetimefilter
    #app.timezone = pytz.timezone('America/Sao_Paulo')
    #app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
    moment = Moment(app)
    #moment.init_app(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:ED6CXnp7qRtrQGTxFYM3jZ@localhost/sap'
    #app.config['SQLALCHEMY_DATABASE_URI'] += '?timezone=utc'  # Definir fuso horário UTC
    #app.config['SQLALCHEMY_DATABASE_URI'] += '?charset=utf8mb4'
    #app.config['SQLALCHEMY_DATABASE_URI'] += '&timezone=utc'  # Definir fuso horário UTC

    # Substitua 'username', 'password' e 'database_name' pelas suas credenciais e nome do banco de dados MySQL
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(PROJECT_ROOT, 'database/imdb.sqlite.db')
    #print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app)

    #e adiciona isso
    app.register_blueprint(maraBp)

    return app

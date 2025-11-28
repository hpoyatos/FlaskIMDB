from flask import Flask, redirect, jsonify
from .extensions import db, migrate
#codigo
from .routes.filmeBp import filmeBp
import os
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(PROJECT_ROOT, 'database/imdb.sqlite.db')
    #print(app.config['SQLALCHEMY_DATABASE_URI'])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app)

    #e adiciona isso
    app.register_blueprint(filmeBp)

    # Redirecionamento padrão da raiz...
    @app.route("/")
    def root_redirect():
        return redirect("/filme", code=302)

    # Para eventuais checagens automáticas da saúde do container/projeto
    @app.route("/healthz")
    def healthcheck():
        return jsonify({"status": "ok"}), 200

    return app

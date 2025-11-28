from ..extensions import db
from flask_sqlalchemy import SQLAlchemy

# Tabela de associação many-to-many
filme_genero = db.Table(
    "filme_genero",
    db.Column("genero_id", db.Integer, db.ForeignKey("genero.id"), primary_key=True),
    db.Column("filme_id", db.Integer, db.ForeignKey("filme.id"), primary_key=True),
)

class Genero(db.Model):
    __tablename__ = "genero"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"<Genero {self.nome}>"

class Filme(db.Model):
    __tablename__ = "filme"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)

    # relação N:N com genero
    generos = db.relationship(
        "Genero",
        secondary=filme_genero,
        backref=db.backref("filmes", lazy="dynamic"),
        lazy="subquery",
    )
    
    def __repr__(self):
        return "<Filme(titulo={}, ano={})>".format(self.titulo, self.ano)

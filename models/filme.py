from ..extensions import db

class Filme(db.Model):
    __tablename__ = "filme"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)

    def __repr__(self):
        return "<Filme(titulo={}, ano={})>".format(self.titulo, self.ano)

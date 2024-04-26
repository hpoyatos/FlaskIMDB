from ..extensions import db

class Mara(db.Model):
    __tablename__ = "MARA"
    MATNR = db.Column(db.String(18), primary_key=True, autoincrement=False)
    MAKTX = db.Column(db.String(255))
    MAKTG = db.Column(db.String(2000))
    ERSDA = db.Column(db.Date)
    LAEDA = db.Column(db.Date)

    def __repr__(self):
        return "<Mara(MAKTX={}, LAEDA={})>".format(self.MAKTX, self.LAEDA)
    
    def getMaras(offset=0, per_page=20):
        return Mara.query.offset(offset).limit(per_page).all()
    
    def getByCodigo(codigo, offset=0, per_page=20):
        return Mara.query.filter_by(MATNR=codigo).all()

    @classmethod
    def getByName(nome, offset=0, per_page=20):
        return Mara.query.offset(offset).limit(per_page).filter_by(MAKTX=nome).all()

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

class FilmeForm(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired()])
    ano = IntegerField("Ano", validators=[DataRequired()])
    generos = SelectMultipleField(
        "Gêneros",
        coerce=int  # recebe IDs como int
    )
    submit = SubmitField("Salvar")

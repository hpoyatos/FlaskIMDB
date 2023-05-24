# adiciona o , render_template
from flask import Blueprint, render_template, request, redirect, url_for
from ..extensions import db
from ..models.filme import Filme
from datetime import date, datetime

#Instanciar o blueprint
filmeBp = Blueprint('filmeBp', __name__)

@filmeBp.route('/filme')
def filme_list():
#    return "Teste"
    #adiciona isso
#    db.create_all()
#   Adiciona o acesso a banco e a chamada ao render_template
    filmes_query = Filme.query.all()
    return render_template('filme_list.html', filmes=filmes_query)

@filmeBp.route('/filme/create')
def create_filme():
    return render_template('filme_create.html')

@filmeBp.route('/filme/add', methods=["POST"])
def add_filme():

    sTitulo = request.form["titulo"]
    iAno = request.form["ano"]

    filme = Filme(titulo=sTitulo, ano=iAno)
    db.session.add(filme)
    db.session.commit()

    return redirect(url_for("filmeBp.filme_list"))

#Chamar o formulário de alteração
@filmeBp.route('/filme/update/<filme_id>')
def update_filme(filme_id=0):
    filme_query = Filme.query.filter_by(id = filme_id).first()
    return render_template('filme_update.html', filme=filme_query) 

#Tratar o update (faz ele no banco)
@filmeBp.route('/filme/upd', methods=["POST"])
def upd_filme():

    iFilme = request.form["id"]
    sTitulo = request.form["titulo"]
    iAno = request.form["ano"]

    filme = Filme.query.filter_by(id = iFilme).first()
    filme.titulo = sTitulo
    filme.ano = iAno
    db.session.add(filme)
    db.session.commit()

    return redirect(url_for("filmeBp.filme_list"))  

#Tratar o apagar (tela de confirmação)
@filmeBp.route('/filme/delete/<filme_id>')
def delete_filme(filme_id=0):
    filme_query = Filme.query.filter_by(id = filme_id).first()
    return render_template('filme_delete.html', filme=filme_query) 

#Para apagar de fato
@filmeBp.route('/filme/dlt', methods=["POST"])
def dlt_filme():

    iFilme = request.form["id"]
    filme = Filme.query.filter_by(id = iFilme).first()
    db.session.delete(filme)
    db.session.commit()

    return redirect(url_for("filmeBp.filme_list"))
  
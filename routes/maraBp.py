# adiciona o , render_template
from flask import Blueprint, render_template, request, redirect, url_for
from flask_paginate import Pagination, get_page_args
from ..extensions import db, StringField, SubmitField, FlaskForm
from ..models.mara import Mara
from datetime import date, datetime

#Instanciar o blueprint
maraBp = Blueprint('maraBp', __name__)

def format_number(num):
    num_str = str(num)
    num_zeros = 18 - len(num_str)
    formatted_num = '0' * num_zeros + num_str
    return formatted_num

class SearchForm(FlaskForm):
    search = StringField('Buscar')
    submit = SubmitField('Enviar')

@maraBp.route('/mara', methods=["GET", "POST"])
def mara_list():
#    return "Teste"
    #adiciona isso
#    db.create_all()
#   Adiciona o acesso a banco e a chamada ao render_template
    search_term = ""
    form = SearchForm()
    if form.validate_on_submit():
        #search_term = format_number(form.search.data)
        search_term = form.search.data
        # Aqui você pode fazer o que quiser com o termo de busca, como pesquisar no banco de dados
        #return f'Você buscou por: {search_term}'

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = Mara.query.count()

    if (search_term != ""):
        maras_query = Mara.getByCodigo(codigo=search_term,offset=offset, per_page=per_page)
    else:
        maras_query = Mara.getMaras(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap4')
    return render_template('mara_list.html', maras=maras_query, form=form, page=page, per_page=per_page, pagination=pagination)

@maraBp.route('/mara/create')
def create_mara():
    return render_template('mara_create.html')

@maraBp.route('/mara/add', methods=["POST"])
def add_mara():

    sMAKTX = request.form["MAKTX"]
    dLAEDA = request.form["LAEDA"]

    mara = Mara(MAKTX=sMAKTX, LAEDA=dLAEDA)
    db.session.add(mara)
    db.session.commit()

    return redirect(url_for("maraBp.mara_list"))

#Chamar o formulário de alteração
@maraBp.route('/mara/update/<matnr>')
def update_mara(matnr=0):
    mara_query = Mara.query.filter_by(MATNR = matnr).first()
    return render_template('mara_update.html', mara=mara_query) 

#Tratar o update (faz ele no banco)
@maraBp.route('/mara/upd', methods=["POST"])
def upd_mara():

    sMATNR = request.form["MATNR"]
    sMAKTX = request.form["MAKTX"]
    dLAEDA = request.form["LAEDA"]

    mara = Mara.query.filter_by(MATNR = sMATNR).first()
    mara.MAKTX = sMAKTX
    mara.LAEDA = dLAEDA
    db.session.add(mara)
    db.session.commit()

    return redirect(url_for("maraBp.mara_list"))  

#Tratar o apagar (tela de confirmação)
@maraBp.route('/mara/delete/<sMATNR>')
def delete_mara(sMATNR=0):
    mara_query = Mara.query.filter_by(MATNR = sMATNR).first()
    return render_template('mara_delete.html', mara=mara_query) 

#Para apagar de fato
@maraBp.route('/mara/dlt', methods=["POST"])
def dlt_mara():

    sMATNR = request.form["MATNR"]
    mara = Mara.query.filter_by(MATNR = sMATNR).first()
    db.session.delete(mara)
    db.session.commit()

    return redirect(url_for("maraBp.mara_list"))
  
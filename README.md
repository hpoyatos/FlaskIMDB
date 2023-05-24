# FlaskIMDB
Exemplo de Python Flask + SQLAlchemy com o objetivo de realizar um CRUD de filmes.




Instalação
clone:

$ git clone https://github.com/hpoyatos/FlaskIMDB.git

$ cd FlaskIMDB

Criar & activar o virtual env e instalar dependências de software:

with venv/virtualenv + pip:

$ python -m venv env  # use `python3 ...` for Python3 on Linux & macOS

$ source env/bin/activate  # usar `.env\Scripts\activate` no Windows

$ pip install -r requirements.txt

ou usando Pipenv:

$ pipenv install --dev
$ pipenv shell

Configure a seguinte variável de ambiente

Unix Bash (Linux, Mac, etc.):

$ export FLASK_APP=FlaskIMDB
$ cd ..
$ flask run
Windows CMD:

> set FLASK_APP=hello
> cd ..
> flask run
Windows PowerShell:

> $env:FLASK_APP = "FlaskIMDB"
> cd ..
> flask run

$ flask run
* Running on http://127.0.0.1:5000/

License
This project is licensed under the MIT License (see the LICENSE file for details).

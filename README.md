# FlaskIMDB
Exemplo de Python Flask + SQLAlchemy com o objetivo de realizar um CRUD de filmes.

![image](https://github.com/hpoyatos/FlaskIMDB/assets/957400/7065fad3-0981-46e6-bf82-3f1d8dc1e540)




PEGUE TAMBÉM A IMAGEM PÚBLICA DOCKER em https://hub.docker.com/repository/docker/hpoyatos/flask_imdb/general

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

Como "setar" a variável de ambiente em Unix Bash (Linux, Mac, etc.) e rodar:
$ export FLASK_APP=FlaskIMDB
$ cd ..
$ flask run

Para "setar" a variável de ambiente no Windows CMD e rodar:
> set FLASK_APP=FlaskIMDB
> cd ..
> flask run

Para "setar" a variável de ambiente no Windows PowerShell e rodar:

> $env:FLASK_APP = "FlaskIMDB"
> cd ..
> flask run

Rodou? Espera-se isso!
* Running on http://127.0.0.1:5000/

License
This project is licensed under the MIT License (see the LICENSE file for details).

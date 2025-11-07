# FROM faz um docker pull buscando uma imagem
# que tem Python 3.14.0 e Linux Alpine 3.22
FROM python:3.14.0-alpine3.22

# [EM BUILD] Diretório de trabalho dentro do container.. se o diretório
# não existir, ele cria antes...
WORKDIR /app

# [EM BUILD] COPY -> copia os arquivos de fora para dentro do container
COPY requirements.txt .

# [EM BUILD] RUN -> RODA o comando ***NO MOMENTO DO BUILD***
RUN pip install -r requirements.txt

# [EM BUILD] Copia tudo exceto o que estiver relacionado
# em .dockerignore
COPY . .

# [EM BUILD] ENV (Environment) ele vai criar uma variável de ambiente
ENV FLASK_APP="FlaskIMDB:create_app()"
ENV FLASK_RUN_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

# [EM RUN] CMD roda o comando no RUN e não
# no build...
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app", "--workers", "2", "--threads", "4", "--timeout", "60"]

# [EM RUN] EXPOSE -> que vai expor a porta
# de rede para ser visualizada do lado de
# fora do container
EXPOSE 5000
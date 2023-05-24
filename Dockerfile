FROM python:3.11.3-alpine3.18
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP=app
WORKDIR /
CMD ["flask", "run", "-h", "0.0.0.0"]
COPY . .
EXPOSE 5000


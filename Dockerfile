FROM python:3.11.3-alpine3.18
WORKDIR /app
COPY requirements.txt . 
RUN pip install -r requirements.txt
COPY . .
ENV FLASK_APP app
WORKDIR /
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
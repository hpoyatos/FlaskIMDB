FROM 3.12.3-bookworm
WORKDIR /app 
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ENV FLASK_APP app
WORKDIR /
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000
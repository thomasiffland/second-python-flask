FROM python:3

COPY . /app
ENV HOME=/app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 9091

ENTRYPOINT ["gunicorn","-b","0.0.0.0:9091","-w","2","app:app"]

FROM python:3.8.5

RUN pip install mysql
RUN pip install mysql-connector
RUN pip install flask==1.1.2
RUN pip install flask-wtf
RUN pip install email_validator
RUN pip install flask-bcrypt
RUN pip install bcrypt
RUN pip install flask-login
RUN pip install gunicorn
RUN pip install textblob==0.15.1
RUN python -m textblob.download_corpora
RUN pip install ajax
RUN pip install twilio


#Bundling Source
COPY . /app

# Setting app directory
WORKDIR /app

ENTRYPOINT [ "python" ]

EXPOSE 5000

CMD [ "app.py" ]

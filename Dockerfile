FROM python:3.7-alpine
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
WORKDIR /code
COPY testd.py testd.py
COPY db_config.py  db_config.py
COPY .env .env
COPY database.py database.py
COPY tests/   /tests/
RUN  ls -la  /*
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

#CMD python testd.py tail to keep the docker container running
CMD tail -f /dev/null
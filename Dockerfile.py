FROM python:3.10-slim-buster
RUN apt-get update \
    && apt-get -y install libpq-dev gcc 
WORKDIR /app
# COPY ./requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
COPY . /app
ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]

FROM python:3.6.8

RUN apt update && apt install unixodbc unixodbc-dev python3-dev -y

ADD . /{{cookiecutter.project_name}}

WORKDIR /{{cookiecutter.project_name}}

RUN pip install -r requirements.txt

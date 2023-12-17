FROM python:3

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY main.py ./
COPY database.py ./

RUN pip install beautifulsoup4
RUN pip install requests
RUN pip install flask
RUN pip install python-telegram-bot==13.7
RUN pip install telebot

CMD python3 parcingbot.py

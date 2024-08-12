FROM python:3.11.6-slim

WORKDIR /app

COPY . ./

CMD [ "python", "./main.py" ]
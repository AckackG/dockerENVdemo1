FROM python:3.11.6-slim

WORKDIR /app

ENV ENV_FROM_DOCKERFILE=123456789
COPY . ./

CMD [ "python", "./main.py" ]
FROM python:3.10

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt

COPY ./app /backend/app
COPY ./composes /backend/composes

ARG PORT
ENV PORT $PORT

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

CMD gunicorn -w 1 --bind 0.0.0.0:$PORT 'app:create_app()' --access-logfile=-

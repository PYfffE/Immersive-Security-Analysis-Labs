FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./composes /code/composes

CMD ["uvicorn", "app.rest:app", "--host", "0.0.0.0", "--port", "8080", "--proxy-headers"]
FROM python:3.10

ARG PORT
ENV PORT $PORT

WORKDIR /backend

COPY ./requirements.txt /backend/requirements.txt
COPY ./app /backend/app
COPY ./scripts /backend/scripts

RUN pip install --no-cache-dir --upgrade -r /backend/requirements.txt

RUN chmod +x /backend/scripts/entrypoint.sh
CMD /backend/scripts/entrypoint.sh

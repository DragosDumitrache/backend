FROM python:3.8

WORKDIR code

COPY pyproject.toml poetry.lock ./
RUN pip install poetry; \
    poetry config virtualenvs.create false; \
    poetry install

EXPOSE 8000/TCP
EXPOSE 8000/UDP
COPY . .

ENV GUNICORN_CMD_ARGS="--workers 5 --threads 5 --error-logfile - --bind 0.0.0.0:8000"
WORKDIR backend
CMD [ "gunicorn", "backend.wsgi:application" ]

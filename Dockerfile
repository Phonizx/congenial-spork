FROM tiangolo/uvicorn-gunicorn-fastapi:latest

ENV PYTHONPATH "${PYTHONPATH}:/"
ENV PORT=8000

RUN pip install --upgrade pip

COPY requirements/requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./app /app

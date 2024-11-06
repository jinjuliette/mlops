FROM python:3.11.10-slim-bookworm

LABEL author="Juliette Jin <juliette.jin@epita.fr>"

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

ADD tp1/main.py main.py
ADD tp1/regression.joblib regression.joblib

CMD ["fastapi", "dev", "main.py", "--port=7026", "--host=0.0.0.0"]


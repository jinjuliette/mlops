FROM python:3.11.10-slim-bookworm

LABEL author="Juliette Jin <juliette.jin@epita.fr>"

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

CMD ["fastapi", "dev", "web_service.py", "--port=8080", "--host=0.0.0.0"]
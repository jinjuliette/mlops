# FROM python:3.11.10-slim
FROM tensorflow/tensorflow:devel

LABEL author="Juliette Jin <juliette.jin@epita.fr>"

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt
RUN pip install Pillow dill

ENV TF_ENABLE_ONEDNN_OPTS=0
ENV CUDA_VISIBLE_DEVICES=""

WORKDIR /app

ADD main.py main.py
ADD navires_classification.joblib navires_classification.joblib

CMD ["fastapi", "run", "main.py", "--port=2607", "--host=0.0.0.0"]


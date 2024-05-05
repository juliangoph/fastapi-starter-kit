FROM python:3.12.2-slim-bookworm

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.8.2 \
  TZ="Asia/Dhaka"

# System deps:
RUN apt-get install -yq tzdata && \
    ln -fs /usr/share/zoneinfo/Asia/Dhaka /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    pip install --upgrade pip && \
    pip install "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false && \
    poetry install --only main

# Creating folders, and files for a project:
COPY . /code

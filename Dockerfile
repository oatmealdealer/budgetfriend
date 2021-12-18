# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.1-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV PIPENV_VENV_IN_PROJECT=1

# Use Pipenv for dependency management
RUN python -m pip install pipenv

WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
COPY app .

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser
RUN pipenv install --deploy --ignore-pipfile

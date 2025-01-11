FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && apt-get install netcat-traditional -y && apt-get autoremove -y && apt-get clean

WORKDIR /opt
COPY ./docker/  /opt/docker/
COPY ./pyproject.toml ./logging.yaml ./uv.lock* /opt/
COPY ./app/  /opt/app/

RUN uv sync --frozen
WORKDIR /opt/app

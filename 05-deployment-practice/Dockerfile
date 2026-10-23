#This is large package, using slim version
#FROM python:3.13

FROM python:3.13.5-slim-bookworm

#This is also large to install uv, using the one below that is recommended by the uv team
#RUN pip install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ".python-version" "pyproject.toml" "uv.lock" ./

RUN uv sync --no-install-project

COPY "predict.py" "model.bin" ./

EXPOSE 9696

ENTRYPOINT ["uv", "run", "--no-sync", "uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
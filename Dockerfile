FROM python:3.12-slim
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt
COPY main ./main
ARG logging_config_file="logging_config.yaml"
COPY ${logging_config_file} ./logging_config.yaml
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]

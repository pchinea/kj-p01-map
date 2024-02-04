FROM python:3-slim as python
ENV PYTHONUNBUFFERED=true
WORKDIR /app

FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | python -
COPY poetry.lock ./poetry.lock
COPY pyproject.toml ./pyproject.toml
RUN poetry install --no-interaction --no-ansi --no-root -vvv
COPY README.md ./README.md
COPY entrypoint.sh ./entrypoint.sh
COPY alembic.ini ./alembic.ini
COPY src ./src

FROM python as runtime
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="src"
COPY --from=poetry /app /app
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["uvicorn", "src.city_map_server.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000
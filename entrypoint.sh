#!/bin/bash

alembic upgrade head
python src/scripts/bulk_load.py
exec "$@"
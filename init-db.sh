#!/bin/bash
# init-db.sh
# Runs automatically on first PostgreSQL container startup (via docker-entrypoint-initdb.d).
# Creates the test database used by pytest integration tests.

set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE fastapi_test_db;
    GRANT ALL PRIVILEGES ON DATABASE fastapi_test_db TO $POSTGRES_USER;
EOSQL

#!/bin/bash

set +ex

ARGS="$@"
DATABASE_URL=postgresql://user:password@127.0.0.1:5432/sessionaway
SECRET_KEY=TEMP

if [[ "$ARGS" == "upgrade" ]]; then
    DATABASE_URL=$DATABASE_URL SECRET_KEY=$SECRET_KEY alembic upgrade head
elif [[ "$ARGS" == "migration "* ]]; then
    ARGS="${ARGS#migration }" # remove "migration " prefix
    DATABASE_URL=$DATABASE_URL SECRET_KEY=$SECRET_KEY alembic revision --autogenerate -m "$ARGS"
elif [[ "$ARGS" == "downgrade" ]]; then
    DATABASE_URL=$DATABASE_URL SECRET_KEY=$SECRET_KEY alembic downgrade -1
else
    echo "Usage: $0 [upgrade|migration <message>|downgrade]"
    exit 1
fi

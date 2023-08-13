#!/bin/bash

hackathon collectstatic --noinput
hackathon migrate

if [ "$DEBUG" = 0 ]; then
  gunicorn src.hackathon.wsgi:application \
    -w 4 \
    -b 0.0.0.0:8000 \
    --error-logfile '-' \
    --log-level debug
else
  hackathon createsuperuser --noinput
  hackathon runserver 0.0.0.0:8000
fi

#!/bin/bash

upstudy collectstatic --noinput
hackathon migrate
"$@"

#!/bin/bash

hackathon collectstatic --noinput
hackathon migrate
"$@"

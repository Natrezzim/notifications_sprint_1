#!/bin/sh

cd /usr/src/app/utils/
python wait_for_raddit.py
cd /usr/src
uvicorn app.main:app --host 0.0.0.0 --port 8010 --access-log
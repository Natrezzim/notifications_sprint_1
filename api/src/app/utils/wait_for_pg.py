import logging
import os
from pathlib import Path

import backoff
import psycopg2
from dotenv import load_dotenv

load_dotenv(f"{Path(os.getcwd())}/.env")

logging.getLogger('backoff').addHandler(logging.StreamHandler())

dsl = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_URL'),
}


@backoff.on_exception(wait_gen=backoff.expo,
                      exception=(psycopg2.Error, psycopg2.OperationalError))
def postgres_conn():
    psycopg2.connect(**dsl)


if __name__ == '__main__':
    postgres_conn()

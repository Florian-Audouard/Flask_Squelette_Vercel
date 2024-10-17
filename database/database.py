"""_summary_

Returns:
    _type_: _description_
"""

import os
import urllib.parse
import psycopg2
from dotenv import dotenv_values
from time import sleep

os.chdir(os.path.dirname(__file__))

ENV_FILENAME = ".env"

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and (sys.argv[0] == "--site" or sys.argv[1] == "--site"):
        ENV_FILENAME = "site.env"

if os.path.exists(ENV_FILENAME):
    config = dotenv_values(ENV_FILENAME)
else:
    config = {
        "USER_DB": os.environ.get("USER_DB"),
        "PASSWORD_DB": os.environ.get("PASSWORD_DB"),
        "HOST_DB": os.environ.get("HOST_DB"),
        "PORT_DB": os.environ.get("PORT_DB"),
        "DATABASE_DB": os.environ.get("DATABASE_DB"),
    }

FILENAME_DB_SHEMA = "database.sql"
options = urllib.parse.quote_plus("--search_path=modern,public")
CONN_PARAMS = f"postgresql://{config['USER_DB']}:{config['PASSWORD_DB']}@{config['HOST_DB']}:{config['PORT_DB']}/{config['DATABASE_DB']}?options={options}"  # pylint: disable=line-too-long


def clean_querry(func):
    def wrapper_func(*args, **kwargs):
        res = ""
        postgres = psycopg2.connect(CONN_PARAMS)
        try:
            with postgres as conn:  # pylint: disable=not-context-manager
                with conn.cursor() as cur:
                    res = func(cur, *args, **kwargs)
        finally:
            postgres.close()
        return res

    return wrapper_func


@clean_querry
def reset_table(cur):  # pylint: disable=missing-function-docstring
    with open(FILENAME_DB_SHEMA, "r", encoding="utf-8") as file:
        cur.execute(file.read())


@clean_querry
def get_data(cur):  # pylint: disable=missing-function-docstring
    cur.execute("select text from data;")
    return cur.fetchall()


@clean_querry
def init_data(cur):
    cur.execute(
        "INSERT INTO data (text) VALUES (%(msg)s);",
        {
            "msg": "Message recu depuis la base de données",
        },
    )


if __name__ == "__main__":
    reset_table()
    init_data()
    print(get_data())

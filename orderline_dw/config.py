"""
Gebruik
-------
Deze module bevat configuratieparameters. Je kunt ze bijvoorbeeld zo gebruiken:

import config

path = config.DATABASES_CONNECTION_STRING_OLTP
"""
import dotenv
import os


# Hier staan de config parameters. Ze worden samengesteld met informatie uit de environment variables.
DATABASES_CONNECTION_STRING_OLTP = None
DATABASES_CONNECTION_STRING_DW = None


def load():
    global DATABASES_CONNECTION_STRING_DW, DATABASES_CONNECTION_STRING_OLTP

    dotenv.load_dotenv()

    oltp_db_server = os.getenv("OLTP_DB_SERVER")
    oltp_db_name = os.getenv("OLTP_DB_NAME")
    oltp_username = os.getenv("OLTP_USERNAME")
    oltp_password = os.getenv("OLTP_PASSWORD")

    dw_db_server = os.getenv("DW_DB_SERVER")
    dw_db_name = os.getenv("DW_DB_NAME")
    dw_username = os.getenv("DW_USERNAME")
    dw_password = os.getenv("DW_PASSWORD")

    DATABASES_CONNECTION_STRING_OLTP = f"mssql+pyodbc://{oltp_username}:{oltp_password}@{oltp_db_server}/{oltp_db_name}?driver=ODBC+Driver+17+for+SQL+Server"
    DATABASES_CONNECTION_STRING_DW = f"mssql+pyodbc://{dw_username}:{dw_password}@{dw_db_server}/{dw_db_name}?driver=ODBC+Driver+17+for+SQL+Server"


# Dit zorgt ervoor dat de parameters worden geladen bij het importeren van deze module.
load()

import logging

import pandas as pd
import sqlalchemy as sa

from orderline_dw import config

logger = logging.getLogger(__name__)

SCHEMA_OLTP = "oltp"
SCHEMA_DW = "staging"
TABLES = ["klant", "productcategorie", "productsubcategorie", "product", "bestelling", "bestellingregel"]


def _copy_tables(engine_oltp, engine_dw):
    global SCHEMA_OLTP, TABLES

    for table in TABLES:
        logger.info(f"Lees de tabel {table} uit oltp.")
        df = pd.read_sql_table(schema=SCHEMA_OLTP, table_name=table, con=engine_oltp)
        logger.info(f"Schrijf de tabel {table} naar staging in het data warehouse.")
        df.to_sql(schema=SCHEMA_DW, name=table, if_exists='replace', index=False, con=engine_dw)


def execute():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    engine_oltp = sa.create_engine(config.DATABASES_CONNECTION_STRING_OLTP)
    engine_dw = sa.create_engine(config.DATABASES_CONNECTION_STRING_DW, fast_executemany=True)
    try:
        _copy_tables(engine_oltp=engine_oltp, engine_dw=engine_dw)
    finally:
        engine_oltp.dispose()
        engine_dw.dispose()


if __name__ == "__main__":
    execute()

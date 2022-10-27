import pandas as pd
import psycopg2
from db_config import DBConfig
from psycopg2._psycopg import connection
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine


class RedshiftDB:
    _engine: Engine = None
    _conn: connection = None
    _db_config: DBConfig

    def __init__(self, engine: Engine, conn: connection, db_config: DBConfig):
        self._engine = engine
        self._conn = conn
        self._db_config = db_config

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):  # noqa
        self.close()

    @classmethod
    def connect(cls, db_config: DBConfig) -> 'RedshiftDB':
        conn = psycopg2.connect(
            dbname=db_config.db_name,
            host=db_config.host,
            port=db_config.port,
            user=db_config.user,
            password=db_config.password)
        db_string = "postgresql://%s:%s@%s:%s/%s" % (
            db_config.user, db_config.password, db_config.host, db_config.port, db_config.db_name
        )
        engine = create_engine(db_string)
        return RedshiftDB(engine, conn, db_config)

    def close(self) -> None:
        self._conn.close()

    def load_query(self, sql_query: str) -> pd.DataFrame:
        """
        Transform a SELECT query into a pandas dataframe
        """
        with self._engine.connect() as conn:
            return pd.read_sql(sql=sql_query, con=conn)

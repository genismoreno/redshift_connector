import logging
import os

import pandas as pd
from db_config import DBConfig
from redshift_db import RedshiftDB


CONFIG = DBConfig.from_env()
TABLE_NAME = os.getenv('REDSHIFT_TABLE_NAME')
JOB_ID = os.getenv('JOB_ID')

logger = logging.getLogger('app')


def main() -> None:
    with RedshiftDB.connect(CONFIG) as db:
        sql_query = f"""
            select *
            from {TABLE_NAME}
            where job_id = '{JOB_ID}'
            """
        logger.debug(sql_query)
        df = db.load_query(sql_query=sql_query)
        with pd.option_context(
                'display.max_rows', None,
                'display.max_columns', None,
                'display.precision', 3,
        ):
            print(df)


if __name__ == '__main__':
    main()

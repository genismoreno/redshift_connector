import argparse
import logging

import pandas as pd
from db_config import DBConfig
from redshift_db import RedshiftDB


CONFIG = DBConfig.from_env()

logger = logging.getLogger('app')


def main(table_name: str, job_id: str) -> None:
    with RedshiftDB.connect(CONFIG) as db:
        sql_query = f"""
            select *
            from {table_name}
            where job_id = '{job_id}'
            limit 50
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
    parser = argparse.ArgumentParser(description='Redshift table rows printer by job id')
    parser.add_argument('table_name', type=str, help='redshift table name')
    parser.add_argument('job_id', type=str, help='job id to filter')

    args = parser.parse_args()

    main(args.table_name, args.job_id)

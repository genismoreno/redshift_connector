import os


class DBConfig:
    user: str
    password: str
    db_name: str
    host: str
    port: int

    def __init__(self, user: str, password: str, db_name: str, host: str, port: int):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port

    @classmethod
    def from_env(cls) -> 'DBConfig':
        return cls(
            user=os.environ['REDSHIFT_USER'],
            password=os.environ['REDSHIFT_PASSWORD'],
            db_name=os.environ['REDSHIFT_DB_NAME'],
            host=os.environ['REDSHIFT_HOST'],
            port=int(os.environ['REDSHIFT_PORT']),
        )

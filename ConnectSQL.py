DB_TYPE = ''
DB_USER = ''
DB_PWD = ''
DB_SERVER = ''
DB_PORT = ''
DB_NAME = ''
DB_DRIVER = ''
conn_string = '{}://{}:{}@{}:{}/{}?driver={}'.format(DB_TYPE, DB_USER, DB_PWD, DB_SERVER, DB_PORT, DB_NAME, DB_DRIVER)
from sqlalchemy import create_engine
engine = create_engine(conn_string)
conn = engine.connect()
from sqlalchemy import inspect
inspector = inspect(engine)
tables = []
for schema in inspector.get_schema_names():
    tables.extend([str(schema)+'.'+str(i) for i in inspector.get_table_names(schema = schema)])

from sqlalchemy import create_engine, text

connection_string = 'postgresql://hbnb_dev:hbnb_dev_pwd@localhost:5432/hbnb_dev_db'

engine = create_engine(connection_string)

with engine.connect() as connection:
    sql_statement = text('SELECT version()')
    result = connection.execute(sql_statement)
    print(result.fetchone()[0])
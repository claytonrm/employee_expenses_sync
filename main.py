from sqlalchemy import create_engine, MetaData
from employee_expenses_sync.model.model import Base


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    url = 'postgresql://{}:{}@{}:{}/{}'
    database_url = url.format(user, password, host, port, db)
    engine = create_engine(database_url, client_encoding='utf8')
    MetaData(bind=engine, reflect=True)

    return engine


def setup_database():
    engine = connect('adm', '12345678', 'employee_expenses')
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    setup_database()
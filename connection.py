from sqlalchemy import create_engine, MetaData
from employee_expenses_sync.model.model import Base


class Connection:

    def connect(self, user, password, db, host='localhost', port=5432):
        url = 'postgresql://{}:{}@{}:{}/{}'
        database_url = url.format(user, password, host, port, db)
        engine = create_engine(database_url, client_encoding='utf8')
        MetaData(bind=engine, reflect=True)

        self.connection = engine

        return engine

    @staticmethod
    def setup_database():
        conn = Connection()
        engine = conn.connect('adm', '12345678', 'employee_expenses')
        Base.metadata.create_all(engine)

    def get_connection(self):
        return self.connection

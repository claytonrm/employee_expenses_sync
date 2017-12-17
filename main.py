import psycopg2
from employee_expenses_sync import settings
from employee_expenses_sync.service.service import Service

if __name__ == '__main__':
    conn = settings.DB_CONN

    try:
        conn = psycopg2.connect(conn)
    except Exception as e:
        print(e)
        print("I am unable to connect to the database.")

    service = Service()

    bar_rows = service.connection_test(conn)

    for row in bar_rows:
        print ("   ", row[0])

    conn.close()

# transparencias = service.get_transparencia(year=2017, month=11)
#
# engine = create_engine('sqlite:///db.sqlite')
# session_factory = sessionmaker()
# session_factory.configure(bind=engine)
# Base.metadata.create_all(engine)
#
# session = session_factory()
#
# for transparencia in transparencias:
#     cursor = session.query(Employee).filter(Employee.cpf == transparencia.cpf)
#     result = cursor.fetchone()
#     if result.rowcount == 0:
#         employee = Employee(name=transparencia.nome, cpf=transparencia.cpf)
#         session.add(employee)
#     else:
#         employee = result[0]
#
#     payroll = Payroll(employee=employee, wage=1324)
#     session.add(payroll)
#     session.commit()
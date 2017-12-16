from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session

from .service import Service
from .model import Employee, Payroll, Base


service = Service()

transparencias = service.get_transparencia(year=2017, month=11)

engine = create_engine('sqlite:///db.sqlite')
session_factory = sessionmaker()
session_factory.configure(bind=engine)
Base.metadata.create_all(engine)

session = session_factory()
for transparencia in transparencias:
    cursor = session.query(Employee).filter(Employee.cpf == transparencia.cpf)
    result = cursor.fetchone()
    if result.rowcount == 0:
        employee = Employee(name=transparencia.nome, cpf=transparencia.cpf)
        session.add(employee)
    else:
        employee = result[0]

    payroll = Payroll(employee=employee, wage=1324)
    session.add(payroll)
    session.commit()
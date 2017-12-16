from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    admission_date = Column(DateTime, nullable=False)

    position_id = Column(Integer, ForeignKey("position.id"))
    organ_id = Column(Integer, ForeignKey("organ.id"))
    division_id = Column(Integer, ForeignKey("division.id"))
    subdivision_id = Column(Integer, ForeignKey("subdivision.id"))
    specialty_id = Column(Integer, ForeignKey("specialty.id"))
    employment_relationship_id = Column(Integer, ForeignKey("employment_relationship.id"))

    position = relationship("Position", foreign_keys=[position_id])
    organ = relationship("Position", foreign_keys=[organ_id])
    division = relationship("Division", foreign_keys=[division_id])
    subdivision = relationship("Subdivision", foreign_keys=[subdivision_id])
    specialty = relationship("Specialty", foreign_keys=[specialty_id])
    employment_relationship = relationship("EmploymentRelationship", foreign_keys=[employment_relationship_id])


class Payroll(Base):
    __tablename__ = 'payroll'

    id = Column(Integer, primary_key=True)
    wage = Column(Numeric, nullable=False)
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    employee = relationship('Employee', foreign_keys=[employee_id])


class Organ(Base):
    __tablename__ = 'organ'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Position(Base):
    __tablename__ = 'position'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Division(Base):
    __tablename__ = 'division'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Subdivision(Base):
    __tablename__ = 'subdivision'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Departament(Base):
    __tablename__ = 'departament'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Specialty(Base):
    __tablename__ = 'specialty'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class EmploymentRelationship(Base):
    __tablename__ = 'employment_relationship'

    id = Column(Integer, primary_key=True)
    name = Column(String)

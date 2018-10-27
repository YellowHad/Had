from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Use default=func.now() to set the default hiring time
    # of an Employee to be the current time when an
    # Employee record was created
    hired_on = Column(DateTime, default=func.now())
    department_id = Column(Integer, ForeignKey('department.id'))
    # Use cascade='delete,all' to propagate the deletion of a Department onto its Employees
    department = relationship(
        Department,
        backref=backref('employees',
                        uselist=True,
                        cascade='delete,all'))


from sqlalchemy import create_engine

engine = create_engine('sqlite:///orm_in_detail.sqlite')

from sqlalchemy.orm import sessionmaker

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)

if __name__ == '__main__':
    raw_input("press enter to continue")

    # department will be connected to employee via a foreign key
    d = Department(name="IT")
    emp1 = Employee(name="John", department=d)
    s = session()
    s.add(d)
    s.add(emp1)
    s.commit()
    s.delete(d)  # Deleting the department also deletes all of its employees.
    s.commit()
    print s.query(Employee).all()

    entered_department = s.query(Department).first()
    print s.query(Employee).filter(Employee.department == entered_department).all()

    # hired_on is only set after commit
    # check the following code:
    emp2 = Employee(name="Marry")
    print emp2.hired_on
    s.add(emp2)
    print emp2.hired_on
    s.commit()
    print emp2.hired_on

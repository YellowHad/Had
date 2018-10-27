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

    IT = Department(name="IT")
    Financial = Department(name="Financial")
    john = Employee(name="John", department=IT)
    marry = Employee(name="marry", department=Financial)

    # add to database
    s = session()
    s.add(IT)
    s.add(Financial)
    s.add(john)
    s.add(marry)
    s.commit()

    # add more to database
    cathy = Employee(name="Cathy", department=Financial)
    s.add(cathy)
    s.commit()

    # to find all the employees whose name starts with "C", we can use startswith()
    found_employee = s.query(Employee).filter(Employee.name.startswith("C")).one()
    print found_employee.name

    # to find all the employees whose name starts with "C" and who also work for the Financial department
    found_employee = s.query(Employee).join(Employee.department).filter(Employee.name.startswith('C'), Department.name == 'Financial').one()
    print found_employee.name

    # to search for employees who are hired before a certain datetime
    found_employees = s.query(Employee).filter(Employee.hired_on > func.now()).count()
    print found_employees

    # Find all employees who have been hired in the past
    found_employees = s.query(Employee).filter(Employee.hired_on < func.now()).count()
    print found_employees

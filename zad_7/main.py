from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Float, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.sql import func
from faker import Faker
import random

Base = declarative_base()
fake = Faker()

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="students")
    grades = relationship("Grades", back_populates="student")

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship("Student", back_populates="group")
    subject = relationship("Subject", back_populates="group")

class Lecturer(Base):
    __tablename__ = "lecturers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = relationship("Subject", back_populates="lecturer")

class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    lecturer_id = Column(Integer, ForeignKey("lecturers.id"))
    lecturer = relationship("Lecturer", back_populates="subject")
    group_id = Column(Integer, ForeignKey("group.id"))
    group = relationship("Group", back_populates="subject")
    grades = relationship("Grades", back_populates="subject")

class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", back_populates="grades")
    subject_id = Column(Integer, ForeignKey("subject.id"))
    subject = relationship("Subject", back_populates="grades")
    value = Column(Float)
    date_received = Column(Date)

engine = create_engine('sqlite:///sqlalchemy_szkoła.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_fake_data():
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()

    lecturers = [Lecturer(name=fake.name()) for _ in range(3)]
    session.add_all(lecturers)
    session.commit()

    subjects = [Subject(name=fake.word(), lecturer=random.choice(lecturers)) for _ in range(5)]
    session.add_all(subjects)
    session.commit()

    students = []
    for _ in range(30):
        student = Student(name=fake.name(), group=random.choice(groups))
        students.append(student)
    session.add_all(students)
    session.commit()

    grades = []
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(5, 20)):
                grade = Grades(value=random.uniform(2, 5), student=student, subject=subject)
                grades.append(grade)
    session.add_all(grades)
    session.commit()

create_fake_data()


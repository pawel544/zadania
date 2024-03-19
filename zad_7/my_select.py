from sqlalchemy import func
from main import *
# 1.
def select_1(session):
    return session.query(Student).join(Grades).group_by(Student).order_by(func.avg(Grades.value).desc()).limit(5).all()

# 2.
def select_2(session, subject_name):
    return session.query(Student).join(Grades).filter(Grades.subject.has(name=subject_name)).group_by(Student).order_by(func.avg(Grades.value).desc()).first()

# 3.
def select_3(session, subject_name):
    return session.query(func.avg(Grades.value)).join(Subject).filter(Subject.name == subject_name).scalar()

# 4.
def select_4(session):
    return session.query(func.avg(Grades.value)).scalar()

# 5.
def select_5(session, lecturer_name):
    return session.query(Subject).join(Lecturer).filter(Lecturer.name == lecturer_name).all()
# 6.
def select_6(session, group_name):
    return session.query(Student).join(Group).filter(Group.name == group_name).all()

# 7.
def select_7(session, group_name, subject_name):
    return session.query(Grades).join(Student).join(Subject).join(Group).filter(Group.name == group_name, Subject.name == subject_name).all()

# 8.
def select_8(session, lecturer_name):
    return session.query(func.avg(Grades.value)).join(Subject).join(Lecturer).filter(Lecturer.name == lecturer_name).scalar()

# 9.
def select_9(session, student_name):
    return session.query(Subject).join(Grades).join(Student).filter(Student.name == student_name, Grades.value >= 3.0).all()

# 10.
def select_10(session, lecturer_name, student_name):
    return session.query(Subject).join(Lecturer).join(Grades).join(Student).filter(Lecturer.name == lecturer_name, Student.name == student_name).all()

from faker import Faker
import random
import sqlite3

fake = Faker()
Faker.seed(0)  # Ustawienie ziarna dla generowania tych samych danych

Groups = ["A", "B", "C"]
Subjects = ["Polish", "Mathematics", "History", "Religion", "Physics", "Chemistry"]

try:
    # Connect to the SQLite database
    with sqlite3.connect('school.db') as conn:
        cursor = conn.cursor()

        # Create tables if not exists
        cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            group_id INTEGER)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Teachers (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            subject TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS Grades (
                            id INTEGER PRIMARY KEY,
                            student_id INTEGER,
                            subject TEXT,
                            grade INTEGER,
                            FOREIGN KEY(student_id) REFERENCES Students(id),
                            FOREIGN KEY(subject) REFERENCES Teachers(subject))''')
        print("Tables created successfully!")

        # Populate Students table
        student_data = []
        for _ in range(50):
            student_name = fake.name()
            group_id = random.randint(1, len(Groups))
            student_data.append((None, student_name, group_id))
        print("Students data generated successfully!")

        cursor.executemany("INSERT INTO Students (id, name, group_id) VALUES (?, ?, ?)", student_data)
        print("Students table populated successfully!")

        # Populate Teachers table
        teacher_data = []
        for subject in Subjects:
            teacher_name = fake.name()
            teacher_data.append((None, teacher_name, subject))
        print("Teachers data generated successfully!")

        cursor.executemany("INSERT INTO Teachers (id, name, subject) VALUES (?, ?, ?)", teacher_data)
        print("Teachers table populated successfully!")

        # Populate Grades table
        grade_data = []
        for student_id in range(1, 51):
            for subject in Subjects:
                for _ in range(random.randint(5, 20)):
                    grade = random.randint(2, 5)
                    grade_data.append((None, student_id, subject, grade))
        print("Grades data generated successfully!")

        cursor.executemany("INSERT INTO Grades (id, student_id, subject, grade) VALUES (?, ?, ?, ?)", grade_data)
        print("Grades table populated successfully!")
        print(grade_data)
        # Commit changes
        conn.commit()
except sqlite3.Error as e:
    print("SQLite error:", e)
except Exception as e:
    print("Error:", e)

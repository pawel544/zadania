SELECT DISTINCT Grades.subject
FROM Grades
JOIN Teachers ON Grades.subject = Teachers.subject
JOIN Students ON Grades.student_id = Students.id
WHERE Teachers.name = 'Jason Carroll' AND Students.name = 'Walter Pratt'


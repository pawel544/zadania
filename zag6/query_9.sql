SELECT DISTINCT Grades.subject
FROM Grades
JOIN Students ON Grades.student_id = Students.id
WHERE Students.name = 'Walter Pratt'

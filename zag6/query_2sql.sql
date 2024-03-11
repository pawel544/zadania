SELECT Students.id, Students.name, AVG(Grades.grade) AS average_grade
FROM Students
JOIN Grades ON Students.id = Grades.student_id
WHERE Grades.subject = 'Polish'
GROUP BY Students.id, Students.name
ORDER BY average_grade DESC
LIMIT 1;

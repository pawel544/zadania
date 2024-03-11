SELECT Students.id, Students.name, AVG(Grades.grade) AS average_grade
FROM Students
JOIN Grades ON Students.id = Grades.student_id
WHERE Grades.subject = 'Polish'
GROUP BY Students.group_id 
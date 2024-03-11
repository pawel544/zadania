SELECT AVG(Grades.grade) AS average_grade
FROM Grades 
JOIN Teachers ON Grades.subject = Teachers.subject 
Where Teachers.name="Jason Carroll" AND Grades.subject= "Religion"